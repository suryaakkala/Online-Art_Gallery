# Generated by Django 5.0 on 2024-01-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='artwork_images/'),
        ),
    ]