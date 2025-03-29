from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Vehicle

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_premium')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_premium')
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('bio', 'profile_picture', 'is_premium')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Profile', {'fields': ('bio', 'profile_picture', 'is_premium')}),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_type', 'make', 'model', 'year', 'nickname')
    list_filter = ('vehicle_type', 'year')
    search_fields = ('user__username', 'make', 'model', 'nickname')
    ordering = ('-created_at',)
