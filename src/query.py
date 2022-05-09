import get, set


def match(chat_id, msg, timetable, reminders):
	if msg.startswith('?'):
		match_get(chat_id, msg[1:], timetable, reminders)
	elif msg.startswith('!'):
		match_set(chat_id, msg[1:])


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


def  match_set(chat_id, query):
	if query in ("тихо", "остановись", "хватит", "заткнись"):
		set.stop_game(chat_id)
	elif query in ("игра", "громко"):
		set.start_game(chat_id)
	elif query == "сколько":
		set.persentage(chat_id)
	elif query.split(' ')[0] == "название":
		set.format(chat_id, ' '.join(query.split(' ')[1:]))
