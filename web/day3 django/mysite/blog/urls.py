from django.urls import path
from . import views

# path('test', views.test) : 주소, 그 주소로 가면 사용되는 함수 명

app_name='blog'
urlpatterns = [
    path('', views.index),
    
#     path('postlist/', views.postlist, name='postlist'),
#     path('<int:pk>/detail/', views.detail, name='detail'),

#     path('addpost/', views.AddPost.as_view(), name='addpost'),
    path('<int:pk>/<mode>/', views.EditPost.as_view(), name='viewblog'),
    
    path('login/', views.LoginView.as_view(), name='login'),
]
