# Generated by Django 4.0.4 on 2022-06-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_remove_unit_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
    ]