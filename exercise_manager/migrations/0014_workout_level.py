# Generated by Django 4.2.3 on 2023-10-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_manager', '0013_alter_workout_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='level',
            field=models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='E', max_length=1),
        ),
    ]
