from datetime import datetime
import functions
from game import game


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