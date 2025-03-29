from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'users'

router = DefaultRouter()
# router.register('', views.UserViewSet)  # We'll add this later when we create the ViewSet

urlpatterns = [
    # Settings and vehicle management URLs (more specific)
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('profile/vehicle/add/', views.vehicle_create, name='vehicle_create'),
    path('profile/vehicle/<int:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('profile/vehicle/<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('profile/vehicle/<int:vehicle_pk>/media/<int:media_pk>/delete/', views.vehicle_media_delete, name='vehicle_media_delete'),
    
    # User profile URL (more general, should be last)
    path('profile/<str:username>/', views.profile_view, name='profile'),
]

urlpatterns += router.urls 