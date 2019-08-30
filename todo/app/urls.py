from django.urls import path
from .views import CreateTask,Home,CreateUser,TaskDetail,DeleteTask,TaskEdit,deleteso,showprofile
from django.contrib.auth import views as auth_views
app_name= 'app'
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('create/',CreateTask.as_view(),name='create'),
    path('signup/',CreateUser.as_view(),name='signup'),
    path('detail/<int:pk>',TaskDetail.as_view(),name='detail'),
    path('delete/<int:pk>',DeleteTask.as_view(),name='delete'),
    path('edit/<int:pk>',TaskEdit.as_view(),name='edit'),
    path('deleteso/',deleteso,name='deleteso'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('show-profile',showprofile,name='show'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='app/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='app/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='app/password_reset_complete.html'
         ),  name='password_reset_complete'),
]
