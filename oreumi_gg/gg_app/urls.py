from django.urls import path
from . import views
 
app_name = 'gg_app'    #score 어플리케이션의 url 호출시 앞의 구분자 사용을 하시려면 작성합시다.
 
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('create/', views.create_post, name='create_post'),       
]