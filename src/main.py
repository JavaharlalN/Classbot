import vk_api, datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import query
from functions import longpoll
from data import Timetable
from reminders import Reminders

while True:
	now = datetime.datetime.now()
	print(now)
	print(str((datetime.datetime.now() - datetime.datetime(2021, 9, 1)).total_seconds() / 315360) + '%')
	timetable = Timetable()
	reminders = Reminders()
	try:
		for event in longpoll.check():
			try:
				if event.type == VkBotEventType.MESSAGE_NEW:
					print(event.chat_id)
					msg = event.message["text"].lower()
					query.match(event.chat_id, msg, timetable, reminders)
			except Exception as exexex:
				print(exexex)
	except KeyboardInterrupt:
		break
	except Exception as excexc:
		print(excexc)
