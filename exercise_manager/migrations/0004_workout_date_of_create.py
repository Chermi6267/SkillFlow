# Generated by Django 4.2.3 on 2023-08-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_manager', '0003_alter_workout_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='date_of_create',
            field=models.DateField(blank=True, null=True),
        ),
    ]
