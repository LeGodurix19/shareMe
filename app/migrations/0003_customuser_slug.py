# Generated by Django 4.2.8 on 2023-12-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_link_linkuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.CharField(default='slug', max_length=30, unique=True),
        ),
    ]
