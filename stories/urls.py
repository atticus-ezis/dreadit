from django.urls import path
from . import views

urlpatterns = [
   path('', views.stories_list, name="story_list"),
   path('<slug:author_slug>/<slug:story_slug>', views.story_read, name="story_read"),
]
