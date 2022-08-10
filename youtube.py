from typing import List
from pytube import YouTube
from dataclasses import dataclass
from platform import system
import os
import subprocess

URL = 'https://www.youtube.com/'
SHORT_URL = 'https://youtu.be/'

def isTrueLink(url):
    if url.startswith(URL) or url.startswith(SHORT_URL):
        return True
    else:
        return False



@dataclass
class VideoMetadata:
    resolution: int
    itag: int
    fps: int


class Parser:
    def __init__(self, url: str) -> None:
        self.yt = YouTube(url)
    
    @property
    def title(self):
        return self.yt.title
    
    def video(self) -> List[VideoMetadata]:
        response = self.yt.streams.filter(type='video', progressive=False)
        videos = []
        for video in response:
            videos.append(
                VideoMetadata(
                    resolution=video.resolution,
                    itag=video.itag,
                    fps=video.fps
                )
            )
        return videos
    
    def download_video(self, itag: int, path: str = None) -> str:
        if not os.path.isdir(path):
            os.makedirs(path)
        content = self.yt.streams.get_by_itag(itag)
        return content.download(output_path=path)
    
    def download_audio(self, path: str = None) -> str:
        if not os.path.isdir(path):
            os.makedirs(path)
        content = self.yt.streams.get_audio_only()
        return content.download(output_path=path, filename_prefix='audio')

    def collect_files(self, video_path: str, audio_path: str):
        if system() == "Windows":
            program = os.path.abspath(r"ffmpeg")
            save_path = video_path.replace("\\video\\", '\\downloads\\')
        else:
            program = "ffmpeg"
            save_path = video_path.replace('/video/', '/downloads/')
        command = [program, '-i', video_path, '-i', audio_path, '-codec', 'copy' , save_path, '-y']
        
        if not os.path.isdir("downloads"):
            os.makedirs("downloads")
        
        subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        os.remove(video_path)
        os.remove(audio_path)
        return save_path