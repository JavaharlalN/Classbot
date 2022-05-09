import get


def match(chat_id, msg, timetable, reminders):
	if msg.startswith('?'):
		match_get(chat_id, msg[1:], timetable, reminders)
	elif msg.startswith('!'):
		pass


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
