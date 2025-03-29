from django.contrib import admin
from .models import Route, RouteWaypoint, RouteLeg, RouteComment

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_date', 'end_date', 'total_distance', 'is_public')
    list_filter = ('is_public', 'start_date')
    search_fields = ('title', 'user__username', 'description')
    ordering = ('-created_at',)

@admin.register(RouteWaypoint)
class RouteWaypointAdmin(admin.ModelAdmin):
    list_display = ('route', 'place', 'order', 'stay_duration')
    list_filter = ('route',)
    search_fields = ('route__title', 'place__name', 'notes')
    ordering = ('route', 'order')

@admin.register(RouteLeg)
class RouteLegAdmin(admin.ModelAdmin):
    list_display = ('route', 'start_waypoint', 'end_waypoint', 'distance', 'duration')
    search_fields = ('route__title',)
    ordering = ('route', 'start_waypoint__order')

@admin.register(RouteComment)
class RouteCommentAdmin(admin.ModelAdmin):
    list_display = ('route', 'user', 'created_at')
    search_fields = ('route__title', 'user__username', 'content')
    ordering = ('-created_at',)
