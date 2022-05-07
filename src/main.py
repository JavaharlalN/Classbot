import vk_api, datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from topsecret import token, longpoll
import query

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, longpoll)


# def change_percentage(event):
#	 hm = (datetime.datetime.now() + datetime.timedelta(hours=6) - datetime.datetime(2021, 9, 1)).total_seconds() / 31536000
#	 if hm >= 1:
#		 print(vk_session.method("messages.getChat", {"chat_id": event.chat_id}))
#		 if event.chat_id:
#			 vk_session.method("messages.editChat", {"chat_id": event.chat_id, "title": "Стальное M&#861;&#834;&#789;&#775;&#781;&#790;&#827;&#803;&#792;&#806;&#804;&#812;&#828;&#810;ыло №11"})
#		 sender(event.chat_id, "Ну вот и всё, прощай лето... 100%")
#	 else:
#		 if event.chat_id:
#			 sender(event.chat_id, f"{hm * 100}%")
#		 else:
#			 vk_session.method("messages.editChat", {"chat_id": event.chat_id, "title": f"С&#861;&#834;&#789;&#775;&#781;&#790;&#827;&#803;&#792;&#806;&#804;&#812;&#828;&#810;тальное M&#861;&#834;&#789;&#775;&#781;&#790;&#827;&#803;&#792;&#806;&#804;&#812;&#828;&#810;ыло №{10 + hm}"})
#			 sender(event.chat_id, f"{hm * 100}%")


while True:
	now = datetime.datetime.now() + datetime.timedelta(hours=3)
	print(now)
	try:
		for event in longpoll.check():
			try:
				if event.type == VkBotEventType.MESSAGE_NEW:
					print(event.chat_id)
					msg = event.message["text"].lower()
					query.match(event.chat_id, msg)
			except Exception as exexex:
				print(exexex)
	except KeyboardInterrupt:
		break
	except Exception as excexc:
		print(excexc)