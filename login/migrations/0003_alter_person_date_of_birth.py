# Generated by Django 5.1.3 on 2024-11-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_person_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
