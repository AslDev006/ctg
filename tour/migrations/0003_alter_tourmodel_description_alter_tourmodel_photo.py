# Generated by Django 5.1.3 on 2024-11-21 09:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_alter_tourmodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourmodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='tourmodel',
            name='photo',
            field=models.ImageField(upload_to='media_tour/'),
        ),
    ]
