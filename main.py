import os
from telebot import TeleBot
from config import telegram_token
import YT
import Buttons
import yt_stream


bot = TeleBot(telegram_token)


def send_message():
    msg = Msg.send_message
    chat_id = Msg.id
    bot.send_message(chat_id, msg)

class User:
    def __init__(self):
        self.data = {}

    def inputUser(self, chat_id):
        self.data[chat_id] = {}


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
    if YT.isTrueLink(mes):
        url = mes.split()[0]
        yt = YT.youtube(url)
        text = yt.title()
        content = yt.video()
        if not yt.isStream():
            markup = Buttons.parseVideo(url,content)
        else:
            markup = Buttons.parseStream(url, content)
        bot.send_message(chat_id, f'[{text}]({url})', parse_mode='markdown', reply_markup=markup)
    else:
        pass


@bot.callback_query_handler(lambda query: True)
def queryParser(query):
    print(query.data)
    cmds = query.data.split()
    chat_id = query.message.chat.id
    if cmds[0] == 'yt':
        if cmds[1] == 'dl':
            try:
                bot.send_message(chat_id, 'Пожайлуста подождите, мы получаем данные с YouTube')
                bot.send_message(chat_id, 'Настоятельно не рекомендуется производить, какие либо' +\
                    ' оперции во избежании просадки производительности системы')
                yt = YT.youtube(cmds[2])
                bot.send_message(chat_id, 'Скачиваем Видео дорожку')
                video = yt.download_content(int(cmds[3]), dl_path='video')
                audio = yt.audio()
                bot.send_message(chat_id, 'Скачиваем Аудио дорожку')
                audio = yt.download_content(audio[0]['itag'], dl_path='audio')
                bot.send_message(chat_id, 'Склеиваем Аудио и Видео дорожку')
                bot.send_message(chat_id, 'Процесс не быстрый, пожалуйста подождите несколько минут')
                save_file = yt.collect_files(video, audio)
                os.remove(video)
                os.remove(audio)
                video_file = open(save_file, 'rb')
                bot.send_message(chat_id, "Идёт загрузка видео в чат")
                bot.send_chat_action(chat_id, 'upload_video', timeout=True)
                bot.send_video(chat_id, video_file)
            except:
                bot.send_message(chat_id, 'Ошибка, что-то пошло не так...')
            finally:
                video_file.close()
                os.remove(save_file)
        elif cmds[1] == 'stream':
            yt = YT.youtube(cmds[2])
            if yt.isStream():
                m3u8_url = yt.getStreamLink()
                title = yt.title()
                m3u8 = yt_stream.get(m3u8_url, title, int(cmds[3]))
                m3u8_file = open(m3u8, 'r')
                bot.send_document(chat_id, m3u8_file)
                m3u8_file.close()
                os.remove(m3u8)
            else:
                bot.send_message(chat_id, 'Похоже стрим по данной ссылке завершился, но вы можете скачать запись стрима')
                content = yt.video()
                markup = Buttons.parseVideo(cmds[2], content)
                bot.send_message(chat_id, f'[{yt.title()}]({cmds[2]})', parse_mode='markdown', reply_markup=markup)



user = User()
bot.polling(none_stop=True)