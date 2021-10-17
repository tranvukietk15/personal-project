# Generated by Django 3.2.8 on 2021-10-15 08:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_day', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_details', models.CharField(max_length=4000)),
                ('position', models.CharField(max_length=50)),
                ('members_count', models.IntegerField(default=1)),
                ('technologies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=30)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile')),
            ],
        ),
    ]