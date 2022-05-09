from functions import sender
from game import game


def start_game(chat_id):
	game.start()
	sender(chat_id, "ладно")


def stop_game(chat_id):
	game.stop()
	sender(chat_id, "ладно")
