# Generated by Django 3.1.2 on 2020-11-10 02:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_app', '0010_contact_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]