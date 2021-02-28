

def help():
    with open('msgs/help.txt', 'r') as f:
        return f.read()


def wait_message():
    return 'Пожалуйста подождите...'


def about_dl_audio():
    return 'Скачиваем аудио дорожку'


def about_dl_video():
    return 'Скачиваем видео дорожку'


def collect_video_and_audio():
    return 'Идёт склеивание аудио и видео дорожек'


