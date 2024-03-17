from django import forms
from .models import VideoLink

class VideoLinkForm(forms.ModelForm):
    class Meta:
        model = VideoLink
        fields = ['url']