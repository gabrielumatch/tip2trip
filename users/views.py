from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import UserProfileForm, VehicleForm, VehicleMediaForm
from .models import Vehicle, VehicleMedia, User

# Create your views here.

@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {
        'profile_user': user_profile,
        'posts': user_profile.posts.select_related('author').prefetch_related('likes', 'comments').order_by('-created_at').all(),
        'vehicles': user_profile.vehicles.all(),
    })

@login_required
def profile_settings(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile_settings')
    else:
        form = UserProfileForm(instance=request.user)
    
    vehicles = request.user.vehicles.all()
    return render(request, 'users/profile_settings.html', {
        'form': form,
        'vehicles': vehicles
    })

@login_required
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                vehicle = form.save(commit=False)
                vehicle.user = request.user
                vehicle.save()

                # Handle multiple media files
                files = request.FILES.getlist('media_files[]')
                captions = request.POST.getlist('media_captions[]')
                media_types = request.POST.getlist('media_types[]')

                for i, file in enumerate(files):
                    caption = captions[i] if i < len(captions) else ''
                    media_type = media_types[i] if i < len(media_types) else ('VIDEO' if 'video' in file.content_type else 'PHOTO')
                    
                    VehicleMedia.objects.create(
                        vehicle=vehicle,
                        file=file,
                        caption=caption,
                        media_type=media_type
                    )

            messages.success(request, 'Vehicle added successfully!')
            return redirect('users:profile_settings')
    else:
        form = VehicleForm()
    
    return render(request, 'users/vehicle_form.html', {'form': form})

@login_required
def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            with transaction.atomic():
                vehicle = form.save()

                # Handle multiple media files
                files = request.FILES.getlist('media_files[]')
                captions = request.POST.getlist('media_captions[]')
                media_types = request.POST.getlist('media_types[]')

                for i, file in enumerate(files):
                    caption = captions[i] if i < len(captions) else ''
                    media_type = media_types[i] if i < len(media_types) else ('VIDEO' if 'video' in file.content_type else 'PHOTO')
                    
                    VehicleMedia.objects.create(
                        vehicle=vehicle,
                        file=file,
                        caption=caption,
                        media_type=media_type
                    )

            messages.success(request, 'Vehicle updated successfully!')
            return redirect('users:profile_settings')
    else:
        form = VehicleForm(instance=vehicle)
    
    return render(request, 'users/vehicle_form.html', {
        'form': form,
        'vehicle': vehicle,
        'vehicle_media': vehicle.media.all()
    })

@login_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, 'Vehicle deleted successfully!')
    return redirect('users:profile_settings')

@login_required
def vehicle_media_delete(request, vehicle_pk, media_pk):
    media = get_object_or_404(VehicleMedia, pk=media_pk, vehicle__pk=vehicle_pk, vehicle__user=request.user)
    if request.method == 'POST':
        media.delete()
        messages.success(request, 'Media deleted successfully!')
    return redirect('users:vehicle_edit', pk=vehicle_pk)
