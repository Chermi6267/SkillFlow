import os
import uuid


def workout_preview_path(instance, filename):
    extension = filename.split('.')[-1]
    workoutPreview_directory = os.path.join('exercise_manager', 'static', 'img', 'workout', 'usersPreview')

    filename = f'{uuid.uuid4()}.{extension}'

    return os.path.join(workoutPreview_directory, filename)

def exercise_img_path(instance, filename):
    extension = filename.split('.')[-1]
    workoutPreview_directory = os.path.join('exercise_manager', 'static', 'img', 'workout', 'exerciseImages')

    filename = f'{uuid.uuid4()}.{extension}'

    return os.path.join(workoutPreview_directory, filename)
    # else:
    #     username = instance.author.username
    #     print(instance.preview)
    #     extension = filename.split('.')[-1]

    #     paths = [
    #         os.path.join(workoutPreview_directory, f'{username}_{workout_id}.jpeg'),
    #         os.path.join(workoutPreview_directory, f'{username}_{workout_id}.jpg'),
    #         os.path.join(workoutPreview_directory, f'{username}_{workout_id}.png'),
    #         os.path.join(workoutPreview_directory, f'{username}_{workout_id}.gif'),
    #         os.path.join(workoutPreview_directory, f'{username}_{workout_id}.bmp'),
    #     ]

    #     existing_paths = [path for path in paths if os.path.exists(path)]

    #     for path in existing_paths:
    #         os.remove(path)

    #     return os.path.join(workoutPreview_directory, f'{username}_{workout_id}.{extension}')