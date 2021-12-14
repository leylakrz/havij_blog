from django.urls import path

from .views import *

urlpatterns = [
    path('post/<int:pk>/', PostsDetail.as_view()),
    path('post/<int:pk>/update/', PostsUpdate.as_view()),
]
