from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('obj/<int:pk>/', index_detail, name='index_detail'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('account/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/info/change/', ChangeUserInfoView.as_view(), name='info_change'),
    path('account/delete_user/', DeleteUserView.as_view(), name='delete_user'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register_done/', RegisterDoneView.as_view(), name='register_done'),
    #path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
]
