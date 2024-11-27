# Generated by Django 5.1.3 on 2024-11-22 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('o', 'Others')], max_length=100)),
                ('date_of_birth', models.DateField()),
                ('hobby', models.CharField(choices=[('S', 'Swimming'), ('R', 'Reading'), ('T', 'Travelling'), ('W', 'Writing'), ('P', 'Painting')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
