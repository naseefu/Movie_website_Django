# Generated by Django 4.2.7 on 2024-01-22 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpassw',
        ),
    ]
