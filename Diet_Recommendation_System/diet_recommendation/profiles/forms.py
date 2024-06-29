from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'weight', 'height', 'dietary_preferences', 'allergies', 'health_goals']
