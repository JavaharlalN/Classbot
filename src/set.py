from datetime import datetime, timedelta
import functions
from game import game
from calendar import monthrange as mrange


def start_game(chat_id):
	game.start()
	functions.sender(chat_id, "ладно")


def stop_game(chat_id):
	game.stop()
	functions.sender(chat_id, "ладно")

def persentage(chat_id):
	hm = (datetime.now() - datetime(2021, 9, 1)).total_seconds() / 31536000
	if hm >= 1:
		functions.sender(chat_id, "Ну вот и всё, прощай лето... 100%")
	else:
		functions.sender(chat_id, str(hm * 100) + '%')
	fmt = functions.get_format(chat_id)
	if fmt:
		functions.vk_session.method("messages.editChat", {
			"chat_id": chat_id,
			"title": format(fmt, str(hm)[2:])
		})
	else:
		functions.sender(chat_id, "формат не установлен")

def format(chat_id, format):
	functions.set_format(chat_id, format)


def reminder(reminders, args):
	today = datetime.today()
	if len(args) == 2:
		value, day = args
		if int(day) <= today:
			month = today.month + 1 - 12 * int(today.month == 12)
			return reminders.add(value, date=(int(day), int(month)))
		return reminders.add(value, date=(int(day), today.month))
	elif len(args) == 3:
		value, day, month = args
		return reminders.add(value, date=(int(day), int(month)))
	elif len(args) == 4:
		value, day, month, hour = args
		return reminders.add(value, date=(int(day), int(month)), time=(int(hour), 0))
	elif len(args) == 5:
		value, day, month, hour, minute = args
		return reminders.add(value, (int(hour), int(minute)), date=(int(day), int(month)))
	return "не понял"
