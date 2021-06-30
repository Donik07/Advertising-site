from django.urls import path

from .views import *

urlpatterns = [
    path('bbs/<int:pk>/comments/', Comments.as_view()),
    path('bbs/<int:pk>/', BbDetailView.as_view()),
    path('bbs/', Bbs.as_view()),
]
