from django import forms
from django.contrib.auth import get_user_model
from .models import Vehicle, VehicleMedia

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Tell us about yourself...'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Email'
            })
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'make', 'model', 'year', 'length', 'nickname', 'image']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Give your vehicle a nickname'
            }),
            'make': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Vehicle Make'
            }),
            'model': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Vehicle Model'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Year'
            }),
            'length': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Length in feet'
            }),
            'vehicle_type': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'accept': 'image/*'
            })
        }

class VehicleMediaForm(forms.ModelForm):
    class Meta:
        model = VehicleMedia
        fields = ['file', 'caption', 'media_type']
        widgets = {
            'caption': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Add a caption to your photo/video'
            }),
            'media_type': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm'
            }),
            'file': forms.FileInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'accept': 'image/*,video/*'
            })
        } 