import vk_api, datetime, pickle
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from math import *
from random import *

vk_session = vk_api.VkApi(token="70c3c8f087f11c6b1c9ae4ea75e3ee8cf814f4e21a6a895e0b65b36e135ec188f39e083c7547cfbda0bbd")
longpoll = VkBotLongPoll(vk_session, 209597192)
game = False
lastLet = ''

data = {"denied": set(), "log": -1, "reminders": [], "homework": []}
try:
    with open("settings", "rb") as f:
        data = pickle.load(f)
except Exception as e:
    print(e)


def sender(iid, text):
    vk_session.method("messages.send", {"chat_id": iid, "message": text, "random_id": 0})


def change_percentage(event):
    hm = (datetime.datetime.now() + datetime.timedelta(hours=6) - datetime.datetime(2021, 9, 1)).total_seconds() / 31536000
    if hm >= 1:
        print(vk_session.method("messages.getChat", {"chat_id": event.chat_id}))
        if event.chat_id in data["denied"]:
            vk_session.method("messages.editChat", {"chat_id": event.chat_id, "title": "Стальное M&#861;&#834;&#789;&#775;&#781;&#790;&#827;&#803;&#792;&#806;&#804;&#812;&#828;&#810;ыло №11"})
        sender(event.chat_id, "Ну вот и всё, прощай лето... 100%")
    else:
        if event.chat_id in data["denied"]:
            sender(event.chat_id, f"{hm * 100}%")
        else:
            vk_session.method("messages.editChat", {"chat_id": event.chat_id, "title": f"С&#861;&#834;&#789;&#775;&#781;&#790;&#827;&#803;&#792;&#806;&#804;&#812;&#828;&#810;тальное M&#861;&#834;&#789;&#775;&#781;&#790;&#827;&#803;&#792;&#806;&#804;&#812;&#828;&#810;ыло №{10 + hm}"})
            sender(event.chat_id, f"{hm * 100}%")


ruWords = set("".split())
usedWords = set()

while True:
    now = datetime.datetime.now() + datetime.timedelta(hours=3)
    print(now)
    try:
        for event in longpoll.check():
            try:
                with open("settings", "wb") as f:
                    pickle.dump(data, f)
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print(event.chat_id)
                    msg = event.message["text"].lower()
                    if msg.isdigit() and game:
                        sender(event.chat_id, int(msg) + 1)
            except Exception as exexex:
                sender(data["log"], f"опа, {exexex}")
    except KeyboardInterrupt:
        break
    except Exception as excexc:
        print(excexc)
