# Generated by Django 3.1.2 on 2020-11-19 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_app', '0011_auto_20201109_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
