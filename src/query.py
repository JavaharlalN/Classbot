import get, main


def sender(cid, text):
	main.vk_session.method("messages.send", {"chat_id": cid, "message": text, "random_id": 0})


def match(chat_id, msg):
	if msg.startswith('?'):
		match_get(chat_id, msg[1:])
	elif msg.startswith('!'):
		pass


def match_get(chat_id, query):
	if query in ("помощь", "команды"):
		get.help(chat_id)
