# Generated by Django 3.1.2 on 2020-11-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_app', '0005_auto_20201106_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(blank=True, upload_to='project_pic'),
        ),
    ]