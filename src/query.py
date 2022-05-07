import get
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from topsecret import token, longpoll

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, longpoll)


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
