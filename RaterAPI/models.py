from django.db import models

class Movie(models.Model): 
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=360)


