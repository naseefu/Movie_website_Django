# Generated by Django 4.2.7 on 2024-01-30 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='username',
            field=models.CharField(default=False, max_length=250),
        ),
    ]
