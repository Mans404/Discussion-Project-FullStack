from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .form import SignUpForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # This returns the user object
            login(request, user)  # Now we pass the user object, not a string
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Make sure 'home' is a valid URL name
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User

    fields = ('first_name','last_name','email')

    template_name = 'my_account.html'

    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
