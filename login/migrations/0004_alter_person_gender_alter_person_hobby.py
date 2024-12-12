# Generated by Django 5.1.3 on 2024-12-09 13:24

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_person_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='hobby',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'Sports'), ('T', 'Travelling'), ('R', 'Reading'), ('P', 'Painting'), ('w', 'Writing')], max_length=9),
        ),
    ]
