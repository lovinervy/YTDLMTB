from pytube import YouTube
import subprocess
from platform import system
from os import makedirs

URL = 'https://www.youtube.com/'
SHORT_URL = 'https://youtu.be/'

def isTrueLink(url):
    if url.startswith(URL) or url.startswith(SHORT_URL):
        return True
    else:
        return False


from pytube import YouTube
from os import rename, path, remove


class youtube:
    def __init__(self, url):
        self.result = None
        self.yt = YouTube(url)
        self.url = url

    def title(self):
        return self.yt.title
    
    def progress(self):
        if self.result:
            return self.result
        else:
            return False

    def video(self):
        all_videos = self.yt.streams.filter(type="video")
        videos = []
        for video in all_videos:
            if (video.mime_type == "video/mp4") and (video.resolution != None):
                data = {
                    'itag': video.itag,
                    'res': video.resolution,
                    'fps': video.fps
                }
                videos.append(data)
        return videos

    def audio(self):
        all_audios = self.yt.streams.filter(type = "audio")
        audios = []
        for audio in all_audios:
            if audio.mime_type == "audio/mp4":
                data = {
                    'itag': audio.itag,
                    'abr': audio.abr
                }
                audios.append(data)
        return audios


    def progress_func(self, chunk, file_handle, bytes_remaining):
        size = self.content_size
        progress = 100 * (1 - bytes_remaining/size)
        self.result = progress
        

    def preparation(self):
        self.dl = YouTube(self.url, on_progress_callback=self.progress_func)


    def download_content(self, itag, dl_path = None):
        content = self.yt.streams.filter().get_by_itag(itag)
        #self.content_size = content.filesize
        abs_path = content.download(dl_path)
        return abs_path

    def download_audio(self):
        content = self.yt.streams.filter().get_audio_only()
        #self.content_size = content.filesize
        abs_path = content.download()
        return abs_path 

    def check_audio(self, itag):
        codec = self.dl.streams.get_by_itag(itag).audio_codec
        return codec


    def collect_files(self, video, audio):

        if system() == "Windows":
            program = path.abspath(r"ffmpeg")
            save_path = video.replace("\\video\\", '\\downloads\\')
        else:
            program = "ffmpeg"
            save_path = video.replace('/video/', '/downloads/')
        command = [program, '-i', video, '-i', audio, f"{save_path}"]
        if not path.isdir("downloads"):
            makedirs("downloads")
        
        subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return save_path


if __name__ == "__main__":
    audio = '/home/lovinervy/Документы/Python/YTDLTB/audio/YY - ftHatsune Miku.mp3'
    video = '/home/lovinervy/Документы/Python/YTDLTB/video/YY - ftHatsune Miku.mp4'
    yt = youtube('https://www.youtube.com/watch?v=TcHvEFxk_78')
    yt.collect_files(video, audio)
    
    