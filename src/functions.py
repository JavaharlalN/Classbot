import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from topsecret import token, longpoll

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, longpoll)


def sender(cid, text):
	vk_session.method("messages.send", {"chat_id": cid, "message": text, "random_id": 0})