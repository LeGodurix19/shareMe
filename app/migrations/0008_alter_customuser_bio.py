# Generated by Django 4.2.8 on 2023-12-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_linkuser_created_remove_linkuser_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
