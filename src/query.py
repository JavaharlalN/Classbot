import get


def match(chat_id, msg):
	if msg.startswith('?'):
		match_get(chat_id, msg[1:])
	elif msg.startswith('!'):
		pass


def match_get(chat_id, query):
	if query in ("помощь", "команды"):
		get.help(chat_id)
	elif query == "сколько":
		get.persentage(chat_id);
