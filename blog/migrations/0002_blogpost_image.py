# Generated by Django 5.1.7 on 2025-03-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='blog_images/default_image.jpg', upload_to='blog_images/'),
        ),
    ]
