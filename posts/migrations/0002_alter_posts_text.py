# Generated by Django 4.1 on 2022-08-27 11:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]