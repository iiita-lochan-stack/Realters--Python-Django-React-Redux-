# Generated by Django 4.0.4 on 2022-05-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(),
        ),
    ]