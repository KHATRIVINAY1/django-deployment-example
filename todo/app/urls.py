from django.urls import path
from .views import CreateTask,Home,CreateUser,TaskDetail,DeleteTask,TaskEdit,deleteso
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
    path('logout/',auth_views.LogoutView.as_view(),name='logout')

]
