from datetime import datetime
from functions import sender, vk_session, get_format
from game import game


def start_game(chat_id):
	game.start()
	sender(chat_id, "ладно")


def stop_game(chat_id):
	game.stop()
	sender(chat_id, "ладно")

def persentage(chat_id):
	hm = (datetime.now() - datetime(2021, 9, 1)).total_seconds() / 31536000
	if hm >= 1:
		sender(chat_id, "Ну вот и всё, прощай лето... 100%")
	else:
		sender(chat_id, str(hm * 100) + '%')
	fmt = get_format(chat_id)
	if fmt:
		vk_session.method("messages.editChat", {
			"chat_id": chat_id,
			"title": format(fmt, str(hm)[2:])
		})
	else:
		sender(chat_id, "формат не установлен")
