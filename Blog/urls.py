from django.urls import  path

from .import views 
app_name = 'Blog'

urlpatterns = [
  path('', views.main, name='main'),

  path('users/', views.users, name='users'),
  path('blogs/',views.posts, name='posts'),
  path('blogs/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),
  path('comment/', views.comment, name='comment'),
  path('categories/', views.categories, name='categories'),
  path('index/',views.index, name='index')


]
