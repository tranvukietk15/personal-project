# Generated by Django 3.2.8 on 2021-10-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avt'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_day',
            field=models.DateField(verbose_name='Birthday'),
        ),
    ]
