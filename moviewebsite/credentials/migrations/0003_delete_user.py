# Generated by Django 4.2.7 on 2024-01-29 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_remove_user_cpassw'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]