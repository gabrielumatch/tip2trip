from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'places'

router = DefaultRouter()
# router.register('', views.PlaceViewSet)  # We'll add this later when we create the ViewSet

urlpatterns = [
    # Add your URL patterns here
]

urlpatterns += router.urls 