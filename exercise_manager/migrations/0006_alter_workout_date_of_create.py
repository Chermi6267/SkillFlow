# Generated by Django 4.2.3 on 2023-08-30 03:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_manager', '0005_alter_workout_date_of_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
