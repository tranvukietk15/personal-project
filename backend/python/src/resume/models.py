from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=50)
    birth_day=models.DateField('date published')

class Experience(models.Model):
    profile=models.ForeignKey(Profile, on_delete=CASCADE)
    project_name=models.CharField(max_length=200)
    project_details=models.CharField(max_length=4000)
    position=models.CharField(max_length=50)
    members_count=models.IntegerField(default=1)
    technologies=ArrayField(
        models.CharField(max_length=50, blank=False),
        size=30
    )
