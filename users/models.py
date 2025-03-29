from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Custom user model for Tip2Trip."""
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Social network fields
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    
    class Meta:
        ordering = ['-date_joined']
        
    def __str__(self):
        return self.username
        
    def follow(self, user):
        """Follow another user if not already following."""
        if user != self:
            self.following.add(user)
            
    def unfollow(self, user):
        """Unfollow another user if currently following."""
        self.following.remove(user)
        
    def is_following(self, user):
        """Check if following another user."""
        return self.following.filter(id=user.id).exists()
        
class Vehicle(models.Model):
    """Model for user's vehicle information."""
    VEHICLE_TYPES = [
        ('MOTORHOME', 'Motorhome'),
        ('RV_CLASS_A', 'RV - Class A'),
        ('RV_CLASS_B', 'RV - Class B'),
        ('RV_CLASS_C', 'RV - Class C'),
        ('TRUCK_CAMPER', 'Truck Camper'),
        ('VAN', 'Van'),
        ('OTHER', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    length = models.DecimalField(max_digits=5, decimal_places=2, help_text='Length in feet')
    nickname = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.nickname})" if self.nickname else f"{self.year} {self.make} {self.model}"

class VehicleMedia(models.Model):
    """Model for vehicle photos and videos."""
    MEDIA_TYPES = [
        ('PHOTO', 'Photo'),
        ('VIDEO', 'Video'),
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='vehicle_media/')
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Vehicle media'
        
    def __str__(self):
        return f"{self.get_media_type_display()} for {self.vehicle}"
