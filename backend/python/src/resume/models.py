from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.html import format_html
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
    path=models.CharField(max_length=50, unique=True)
    name=models.CharField(max_length=50)
    birth_day=models.DateField('Birthday')
    avatar=models.ImageField(upload_to='images/', null=True, blank=True)
    degree=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=100, null=True)
    phone=models.CharField(max_length=13, null=True)
    city=models.CharField(max_length=250, null=True)
    introduce=models.CharField(max_length=4000, null=True)
    abount_me=models.CharField(max_length=8000, null=True)

    def admin_image(self):
        return format_html(f'<img src="{self.avatar.url}" style="width: 45px; height:45px;" />')
    admin_image.allow_tags = True

    def __str__(self):
        return self.name

class Experience(models.Model):
    profile=models.ForeignKey(Profile, on_delete=CASCADE)
    company_name=models.CharField(max_length=200, default='')
    project_name=models.CharField(max_length=200)
    project_details=models.CharField(max_length=4000)
    position=models.CharField(max_length=50)
    members_count=models.IntegerField(default=1)
    from_date=models.DateField('From')
    to_date=models.DateField('To')
    responsibility=models.CharField(max_length=2000, null=True)
    technologies=ArrayField(
        models.CharField(max_length=50, blank=False),
        size=30
    )

    def __str__(self):
        return self.company_name

class CategorySkill(models.Model):
    profile=models.ForeignKey(Profile, on_delete=CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return (self.name, self.profile.name)

class Skill(models.Model):
    category=models.ForeignKey(CategorySkill, on_delete=CASCADE)
    name=models.CharField(max_length=100)
    experience_month=models.IntegerField(default=0)

    def __str__(self):
        return [self.name]
