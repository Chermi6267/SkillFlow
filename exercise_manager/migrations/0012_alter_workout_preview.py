# Generated by Django 4.2.3 on 2023-10-29 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_manager', '0011_workout_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='preview',
            field=models.ImageField(blank=True, default='sfsf', upload_to='exercise_manager/static/img/workout/usersPreview'),
        ),
    ]
