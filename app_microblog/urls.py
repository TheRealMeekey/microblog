from django.urls import path
from app_microblog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
