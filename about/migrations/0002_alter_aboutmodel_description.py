# Generated by Django 5.1.3 on 2024-11-21 09:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
