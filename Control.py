

class User:
    def __init__(self):
        self.chat = {}


    def isChat(self, chat_id):
        if chat_id in self.chat:
            return True
        else:
            return False


    def addChat(self, chat_id):
        self.chat[chat_id] = {}
        self.chat[chat_id]['yt'] = False
        self.chat[chat_id]['dl'] = False
        self.chat[chat_id]['count'] = 0
        self.chat[chat_id]['time'] = 0


    def addYouTubeLinl(self, chat_id, link):
        self.chat[chat_id]['yt'] = link


    def removeYouTubeLink(self, chat_id, link):
        self.chat[chat_id]['yt'] = False


    def addDLStatus(self, chat_id):
        self.chat[chat_id]['dl'] = True


    def removeDLStatus(self, chat_id):
        self.chat[chat_id]['dl'] = False


    def countRestNumDL(self, chat_id):
        return self.chat[chat_id]['count']


    def subtractCont(self, chat_id):
        self.chat[chat_id]['count'] -= 1


    def updateCount(self, chat_id, num):
        self.chat[chat_id]['count'] = num


    def updateTimeCount(self, chat_id, time):
        self.chat[chat_id]['time'] = time

