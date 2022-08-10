import os
from telebot import TeleBot
from config import telegram_token
from pytube import exceptions
import youtube
import Buttons


bot = TeleBot(telegram_token)


@bot.message_handler(commands = ['help'])
def helpMessage(msg):
    chat_id = msg.chat.id
    with open('msgs/help.txt', 'r', encoding='utf-8') as f:
        message = f.read()
    bot.send_message(chat_id, message, parse_mode='markdown')


@bot.message_handler(func = lambda msg: msg.content_type == 'text')
def msgParser(msg):
    chat_id = msg.chat.id
    mes = msg.text
    if youtube.isTrueLink(mes):
        url = mes.split()[0]
        yt = youtube.Parser(url)
        text = yt.title
        try:
            content = yt.video()
        except exceptions.LiveStreamError:
            bot.send_message(chat_id, 'Нельзя скачивать активные трансляции')
        else:
            markup = Buttons.parseVideo(url,content)
            bot.send_message(chat_id, f'[{text}]({url})', parse_mode='markdown', reply_markup=markup)


@bot.callback_query_handler(lambda query: True)
def queryParser(query):
    print(query.data)
    cmds = query.data.split()
    chat_id = query.message.chat.id
    if cmds[0] == 'yt':
        if cmds[1] == 'dl':
            try:
                bot.send_message(chat_id, 'Пожайлуста подождите, мы получаем данные с YouTube')
                yt = youtube.Parser(cmds[2])
                bot.send_message(chat_id, 'Скачиваем Видео дорожку')
                video = yt.download_video(int(cmds[3]), path='video')
                bot.send_message(chat_id, 'Скачиваем Аудио дорожку')
                audio = yt.download_audio(path='audio')
                bot.send_message(chat_id, 'Склеиваем Аудио и Видео дорожку')
                save_file = yt.collect_files(video, audio)
                video_file = open(save_file, 'rb')
                bot.send_message(chat_id, "Идёт загрузка видео в чат")
                bot.send_chat_action(chat_id, action='upload_video')
                bot.send_video(chat_id, video_file)
            except:
                bot.send_message(chat_id, 'Ошибка, что-то пошло не так...')
            finally:
                video_file.close()
                os.remove(save_file)


bot.polling(none_stop=True)