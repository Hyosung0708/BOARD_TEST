from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    #read
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    #create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),



]