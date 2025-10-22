from django import forms
from .models import Film, Review

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
