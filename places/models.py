from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User

class Place(models.Model):
    """Model for storing place information."""
    name = models.CharField(max_length=255)
    google_place_id = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    place_type = models.CharField(max_length=100)  # e.g., campground, rv_park, tourist_attraction
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['google_place_id']),
            models.Index(fields=['latitude', 'longitude']),
        ]

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        """Calculate the average rating for this place."""
        ratings = self.visits.filter(rating__isnull=False).values_list('rating', flat=True)
        return sum(ratings) / len(ratings) if ratings else 0

class PlaceVisit(models.Model):
    """Model for recording user visits to places."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='place_visits')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
    )
    review = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-visit_date']
        indexes = [
            models.Index(fields=['user', 'place']),
            models.Index(fields=['visit_date']),
        ]

    def __str__(self):
        return f"{self.user.username} visited {self.place.name} on {self.visit_date}"

class PlacePhoto(models.Model):
    """Model for storing photos of places."""
    visit = models.ForeignKey(PlaceVisit, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='place_photos/')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Photo from {self.visit.place.name} by {self.visit.user.username}"

class PlaceAmenity(models.Model):
    """Model for tracking amenities available at places."""
    AMENITY_TYPES = [
        ('HOOKUPS', 'Full Hookups'),
        ('WATER', 'Water Available'),
        ('ELECTRIC', 'Electric Available'),
        ('DUMP_STATION', 'Dump Station'),
        ('WIFI', 'Wi-Fi'),
        ('SHOWERS', 'Showers'),
        ('LAUNDRY', 'Laundry'),
        ('POOL', 'Swimming Pool'),
        ('PLAYGROUND', 'Playground'),
        ('PET_FRIENDLY', 'Pet Friendly'),
        ('STORE', 'Store'),
        ('RESTAURANT', 'Restaurant'),
    ]

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='amenities')
    amenity_type = models.CharField(max_length=50, choices=AMENITY_TYPES)
    details = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['place', 'amenity_type']
        ordering = ['amenity_type']

    def __str__(self):
        return f"{self.get_amenity_type_display()} at {self.place.name}"
