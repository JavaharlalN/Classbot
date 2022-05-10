from functions import sender
from game import game
import get, set


def match(chat_id, msg, timetable, reminders):
	msg = msg.lower()
	if msg.startswith('?'):
		match_get(chat_id, msg[1:], timetable, reminders)
	elif msg.startswith('!'):
		match_set(chat_id, msg[1:], reminders, timetable)
	elif game.active:
		sender(chat_id, game.reply(msg))


def match_get(chat_id, query, timetable, reminders):
	if query in ("помощь", "команды"):
		get.help(chat_id)
	elif query == "сколько":
		get.persentage(chat_id);
	elif query == "дз":
		get.nearest_hw(chat_id, timetable)
	elif query.startswith("дз") and len(query.split('.')) > 1:
		get.homework(chat_id, timetable, query.split('.')[1:])
	elif query == "напоминания":
		get.reminders(chat_id, reminders)
	elif query in get.weekdays:
		get.timetable(chat_id, get.weekdays[query], timetable)


def  match_set(chat_id, query, reminders, timetable):
	try:
		if query in ("тихо", "остановись", "хватит", "заткнись"):
			set.stop_game(chat_id)
		elif query in ("игра", "громко"):
			set.start_game(chat_id)
		elif query == "сколько":
			set.persentage(chat_id)
		elif query.split(' ')[0] == "название":
			set.name_format(chat_id, ' '.join(query.split(' ')[1:]))
		elif query.startswith("напомнить"):
			sender(chat_id, set.reminder(reminders, query.split('.')[1:]))
		elif query.startswith("напоминать"):
			sender(chat_id, set.periodic(reminders, query.split('.')[1:]))
		elif query.startswith("дз"):
			set.homework(chat_id, query.split('.')[1:], timetable)
	except Exception as e:
		print(e)
		sender(chat_id, "невозможно")
