import get


def match(chat_id, msg, timetable):
	if msg.startswith('?'):
		match_get(chat_id, msg[1:], timetable)
	elif msg.startswith('!'):
		pass


def match_get(chat_id, query, timetable):
	if query in ("помощь", "команды"):
		get.help(chat_id)
	elif query == "сколько":
		get.persentage(chat_id);
	elif query == "дз":
		get.nearest_hw(chat_id, timetable)
