# Generated by Django 5.1.3 on 2024-11-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourmodel',
            name='photo',
            field=models.ImageField(upload_to='media/media_tour/'),
        ),
    ]
