from concurrent.futures import thread
import vk_api, datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import query
from functions import longpoll, reminders_sender
from data import Timetable
from reminders import Reminders
import threading

timetable = Timetable()
reminders = Reminders()

threading.Thread(target=reminders_sender, args=(reminders))

while True:
	now = datetime.datetime.now()
	print(now)
	print(str((datetime.datetime.now() - datetime.datetime(2021, 9, 1)).total_seconds() / 315360) + '%')
	try:
		for event in longpoll.check():
			try:
				if event.type == VkBotEventType.MESSAGE_NEW:
					with open("id", 'w') as f:
						f.write(str(event.chat_id))
					print(event.chat_id)
					msg = event.message["text"].lower()
					query.match(event.chat_id, msg, timetable, reminders. is_game)
			except Exception as exexex:
				print(exexex)
	except KeyboardInterrupt:
		break
	except Exception as excexc:
		print(excexc)