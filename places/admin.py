from django.contrib import admin
from .models import Place, PlaceVisit, PlacePhoto, PlaceAmenity

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_type', 'address', 'latitude', 'longitude')
    list_filter = ('place_type',)
    search_fields = ('name', 'address', 'google_place_id')
    ordering = ('name',)

@admin.register(PlaceVisit)
class PlaceVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'visit_date', 'end_date', 'rating', 'is_public')
    list_filter = ('rating', 'is_public', 'visit_date')
    search_fields = ('user__username', 'place__name', 'review')
    ordering = ('-visit_date',)

@admin.register(PlacePhoto)
class PlacePhotoAdmin(admin.ModelAdmin):
    list_display = ('visit', 'caption', 'created_at')
    search_fields = ('visit__place__name', 'visit__user__username', 'caption')
    ordering = ('-created_at',)

@admin.register(PlaceAmenity)
class PlaceAmenityAdmin(admin.ModelAdmin):
    list_display = ('place', 'amenity_type', 'details', 'is_verified')
    list_filter = ('amenity_type', 'is_verified')
    search_fields = ('place__name', 'details')
    ordering = ('place', 'amenity_type')
