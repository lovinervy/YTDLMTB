import os
from telebot import TeleBot
from config import telegram_token
import YT
import Buttons


bot = TeleBot(telegram_token)


class User:
    def __init__(self):
        self.data = {}

    def inputUser(self, chat_id):
        self.data[chat_id] = {}



@bot.message_handler(commands = ['help'])
def helpMessage(msg):
    chat_id = msg.chat.id
    message = 'Help commands'
    bot.send_message(chat_id, message)


@bot.message_handler(func = lambda msg: msg.content_type == 'text')
def msgParser(msg):
    chat_id = msg.chat.id
    mes = msg.text
    if YT.isTrueLink(mes):
        url = mes.split()[0]
        yt = YT.youtube(url)
        content = yt.video()
        text = yt.title()
        markup = Buttons.parseVideo(url,content)
        bot.send_message(chat_id, f'[{text}]({url})',parse_mode='markdown',reply_markup=markup)
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
                bot.send_message(chat_id, 'Please wait, we are geting data from YouTube')
                yt = YT.youtube(cmds[2])
                bot.send_message(chat_id, 'Download the Video track')
                video = yt.download_content(int(cmds[3]), dl_path='video')
                audio = yt.audio()
                bot.send_message(chat_id, 'Download the Audio track')
                audio = yt.download_content(audio[0]['itag'], dl_path='audio')
                bot.send_message(chat_id, 'Collect Video and Audio track')
                save_file = yt.collect_files(video, audio)
                os.remove(video)
                os.remove(audio)
                video_file = open(save_file, 'rb')
                bot.send_message(chat_id, "Uploading video, please wait and don't push any button")
                bot.send_chat_action(chat_id, 'upload_video', timeout=True)
                bot.send_video(chat_id, video_file)
            except:
                bot.send_message(chat_id, 'Error disconected server, im sorry...')
            finally:
                video_file.close()
                os.remove(save_file)



user = User()
bot.polling(none_stop=True)