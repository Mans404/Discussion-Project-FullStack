from . import views
from django.urls import path
urlpatterns = [
path('',views.home,name = 'home'),
path('about',views.about,name = 'about'),
path('Board/<int:board_id>',views.Board_Topics, name = 'Topics'),
path('Board/<int:board_id>/new',views.new_Topics,name = 'newTopic'),
path('Board/<int:board_id>/topics/<int:topic_id>',views.topic_posts, name = 'topic_posts'),
path('Board/<int:board_id>/topics/<int:topic_id>/reply',views.reply_topic, name = 'reply_topic'),

]