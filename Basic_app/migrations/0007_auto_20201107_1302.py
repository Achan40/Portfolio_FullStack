# Generated by Django 3.1.2 on 2020-11-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_app', '0006_auto_20201106_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
    ]
