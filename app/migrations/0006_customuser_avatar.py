# Generated by Django 4.2.8 on 2023-12-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_link_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='static/shareMe/avatars/default.png', upload_to='static/shareMe/avatars/'),
        ),
    ]