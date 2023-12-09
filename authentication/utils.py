import os

def user_avatar_path(instance, filename):

    username = instance.user.username

    extension = filename.split('.')[-1]

    avatar_directory = os.path.join('authentication', 'static', 'media', 'avatars')

    paths = [
        os.path.join(avatar_directory, f'{username}.jpeg'),
        os.path.join(avatar_directory, f'{username}.jpg'),
        os.path.join(avatar_directory, f'{username}.png'),
        os.path.join(avatar_directory, f'{username}.gif'),
        os.path.join(avatar_directory, f'{username}.bmp'),
    ]

    existing_paths = [path for path in paths if os.path.exists(path)]

    for path in existing_paths:
        os.remove(path)

    return os.path.join(avatar_directory, f'{username}.{extension}')