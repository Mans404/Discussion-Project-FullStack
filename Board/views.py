from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Boards, Topics, Posts
from django.contrib.auth.models import User
from .Forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def home(request):
    boards = Boards.objects.all()
    return render(request, 'home.html', {'boards': boards})

def about(request):
    return HttpResponse('my name is mans')

def Board_Topics(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    queryset = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
    page = request.GET.get('page',1)
    paginator = Paginator(queryset,20)

    try:
        topics = paginator.page(page)

    except PageNotAnInteger:
        topics = paginator.page(1)

    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    return render(request, 'topics.html', {'board': board, 'topics': topics})

@login_required
def new_Topics(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Posts.objects.create(
                message=form.cleaned_data.get("message"),
                created_by=request.user,
                topic=topic
            )
            return redirect('Topics', board_id=board.pk)
    else:
        form = NewTopicForm()
    
    return render(request, 'NewTopic.html', {'board': board, 'form': form})

def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topics, board__pk=board_id, pk=topic_id)
    topic.views += 1
    topic.save()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            messages.success(request, 'Your reply has been posted!')
            return redirect('topic_posts', board_id=board_id, topic_id=topic_id)
    else:
        form = PostForm()
    
    return render(request, 'topic_posts.html', {
        'topic': topic,
        'form': form
    })

@login_required
def reply_topic(request, board_id, topic_id):
    topic = get_object_or_404(Topics, board__pk=board_id, pk=topic_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            messages.success(request, 'Your reply has been posted!')
            return redirect('topic_posts', board_id=board_id, topic_id=topic_id)
    else:
        form = PostForm()
    
    return render(request, 'reply_topic.html', {
        'topic': topic,
        'form': form
    })
