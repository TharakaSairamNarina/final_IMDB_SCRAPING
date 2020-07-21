from django import forms
from .models import Movie_Data,TimeSpan

class Movie_Data_Form(forms.ModelForm):
    class Meta:
        model=Telugu_Movie
        fields=('key','language','gener','sort','id_no','time','img_url','movie','rating','votes','date','duration','character','director','introduction')

class TimeSpan_Form(forms.ModelForm):
    class Meta:
        model=TimeSpan
        fields=('key','time')
