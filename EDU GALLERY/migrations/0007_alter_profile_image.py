# Generated by Django 4.1.3 on 2024-01-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDUGALLERY', '0006_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/def.jpg', upload_to='static/img'),
        ),
    ]
