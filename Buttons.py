from typing import List
from telebot import types

from youtube import VideoMetadata



def inlineButtons(data:list):
    btns = types.InlineKeyboardMarkup(row_width=2)
    btns.add(*data)
    return btns


def parseVideo(link, videos:List[VideoMetadata]):
    btns = []
    res = []
    for video in videos:
        if video.itag > 100 and video.resolution not in res:
            text = f"{video.resolution} {video.fps}fps"
            data = f"yt dl {link} {video.itag}"
            tmp = types.InlineKeyboardButton(text, callback_data=data)
            res.append(video.resolution)
            btns.append(tmp)
    return inlineButtons(btns)
