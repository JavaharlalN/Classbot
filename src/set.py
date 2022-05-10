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
		print(fmt.format(str(hm)[2:]))
		functions.vk_session.method("messages.editChat", {
			"chat_id": chat_id,
			"title": format(fmt.format(str(hm)[2:]))
		})
	else:
		functions.sender(chat_id, "формат не установлен")

def name_format(chat_id, format):
	functions.set_format(chat_id, format)


def reminder(reminders, args):
	today = datetime.today()
	if len(args) == 2:
		value, day = args
		if int(day) <= today.day:
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


def periodic(reminders, args):
	if len(args) == 1:
		return reminders.add(args[0], period=1)
	elif len(args) == 2:
		return reminders.add(args[0], period=int(args[1]))
	elif len(args) == 3:
		value, period, hour = args
		return reminders.add(value, (int(hour), 0), int(period))
	elif len(args) == 4:
		v, p, h, m = args
		return reminders.add(v, (int(h), int(m)), int(p))
	return "не понял"


def homework(chat_id, args, timetable):
	if len(args) == 2:
		functions.sender(chat_id, timetable.add_next(args[0], args[1]))
	elif len(args) == 4:
		l, d, m, v = args
		functions.sender(chat_id, timetable.add(l, d, m, v))
