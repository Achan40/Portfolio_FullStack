# Generated by Django 3.1.2 on 2020-11-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_app', '0003_project_project_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(null=True, upload_to='project_pic/'),
        ),
    ]
