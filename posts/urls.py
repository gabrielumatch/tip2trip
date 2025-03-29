from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'posts'

router = DefaultRouter()
# router.register('', views.PostViewSet)  # We'll add this later when we create the ViewSet

urlpatterns = [
    path('create/', views.create_post, name='create'),
    path('<int:post_id>/like/', views.like_post, name='like'),
    path('<int:post_id>/comment/', views.add_comment, name='comment'),
    path('<int:post_id>/comments/', views.get_post_comments, name='get_comments'),
]

urlpatterns += router.urls 