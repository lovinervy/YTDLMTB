from telebot import types



def inlineButtons(data:list):
    btns = types.InlineKeyboardMarkup(row_width=2)
    btns.add(*data)
    return btns


def parseVideo(link, videos:list):
    btns = []
    res = []
    for video in videos:
        if video['itag'] > 100 and video['res'] not in res:
            text = f"{video['res']} {video['fps']}fps"
            data = f"yt dl {link} {video['itag']}"
            tmp = types.InlineKeyboardButton(text, callback_data=data)
            res.append(video['res'])
            btns.append(tmp)
    return inlineButtons(btns)


def parseStream(link, videos: list):
    btns = []
    res = []
    for video in videos:
        if video['itag'] > 100 and video['res'] not in res:
            text = f"{video['res']} {video['fps']}fps"
            data = f"yt stream {link} {video['res'][:-1]}"
            tmp = types.InlineKeyboardButton(text, callback_data=data)
            res.append(video['res'])
            btns.append(tmp)
    return inlineButtons(btns)   
    

