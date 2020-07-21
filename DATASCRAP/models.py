from django.db import models

class TimeSpan(models.Model):
    key=models.CharField(max_length=50)
    time=models.DateTimeField()

class Movie_Data(models.Model):
    key=models.CharField(max_length=50)
    language=models.CharField(max_length=15)
    gener=models.CharField(max_length=15)
    sort=models.CharField(max_length=15)
    img_url=models.CharField(max_length=500)
    movie=models.CharField(max_length=30)
    rating=models.CharField(max_length=10)
    votes=models.CharField(max_length=10)
    date=models.CharField(max_length=15)
    duration=models.CharField(max_length=10)
    character=models.CharField(max_length=200)
    director=models.CharField(max_length=100)
    introduction=models.CharField(max_length=200)

