import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from topsecret import token, longpoll

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, longpoll)


def sender(cid, text):
	vk_session.method("messages.send", {"chat_id": cid, "message": text, "random_id": 0})


def get_format(chat_id):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXIST chats (format text, chat_id int)")
	con.commit()
	cur.execute(f"SELECT format FROM chats WHERE chat_id={chat_id}")
	res = cur.fetchone()
	con.close()
	return res


def set_format(chat_id, format):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXIST chats (format text, chat_id int)")
	con.commit()
	cur.execute(f"UPDATE chats SET format={format} WHERE chat_id={chat_id}")
	con.commit()
	con.close()
