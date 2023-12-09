# Generated by Django 4.2.3 on 2023-10-29 03:43

from django.db import migrations, models
import exercise_manager.utils


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_manager', '0012_alter_workout_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='preview',
            field=models.ImageField(blank=True, default='exercise_manager/static/img/image.svg', upload_to=exercise_manager.utils.workout_preview_path),
        ),
    ]
