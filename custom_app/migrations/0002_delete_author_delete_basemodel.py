# Generated by Django 4.1.7 on 2023-03-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='BaseModel',
        ),
    ]
