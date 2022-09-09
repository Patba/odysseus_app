import os


def get_root_dir() -> str:
    return os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def get_odysseus_img() -> str:
    return os.path.join(get_root_dir(), 'static', 'assets', 'img', 'odysseus_logo_message.png')