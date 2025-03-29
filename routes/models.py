from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User
from places.models import Place

class Route(models.Model):
    """Model for storing trip routes."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routes')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    total_distance = models.DecimalField(max_digits=10, decimal_places=2, help_text='Distance in miles')
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class RouteWaypoint(models.Model):
    """Model for storing waypoints in a route."""
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='waypoints')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='route_waypoints')
    order = models.PositiveIntegerField()
    stay_duration = models.PositiveIntegerField(null=True, blank=True, help_text='Duration of stay in days')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['route', 'order']
        unique_together = ['route', 'order']

    def __str__(self):
        return f"Stop {self.order} at {self.place.name} on {self.route.title}"

class RouteLeg(models.Model):
    """Model for storing route segments between waypoints."""
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='legs')
    start_waypoint = models.ForeignKey(RouteWaypoint, on_delete=models.CASCADE, related_name='legs_as_start')
    end_waypoint = models.ForeignKey(RouteWaypoint, on_delete=models.CASCADE, related_name='legs_as_end')
    distance = models.DecimalField(max_digits=8, decimal_places=2, help_text='Distance in miles')
    duration = models.PositiveIntegerField(help_text='Estimated duration in minutes')
    polyline = models.TextField(help_text='Encoded polyline string for the route segment')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['route', 'start_waypoint__order']

    def __str__(self):
        return f"Leg from {self.start_waypoint.place.name} to {self.end_waypoint.place.name}"

class RouteComment(models.Model):
    """Model for storing comments on routes."""
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='route_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.route.title}"
