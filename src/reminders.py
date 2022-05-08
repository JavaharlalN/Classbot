import sqlite3


class Reminders:
	def __init__(self):
		self.reminders = []  # tuple(value, (day, month), id, (hour, minute))
		self.periodic = []  # tuple(value, id, (hour, minute))

	def save(self):
		con = sqlite3.connect("data.db")
		cur = con.cursor()
		cur.execute("TRUNCATE TABLE IF EXIST reminders")
		cur.execute("TRUNCATE TABLE IF EXIST periodic")
		cur.execute(f"""CREATE TABLE IF NOT EXIST reminders
							(value text, date text, time text)""")
		cur.execute(f"""CREATE TABLE IF NOT EXIST periodic
							(value text, time text)""")
		cur.commit()
		for lesson in self.monday:
			cur.execute(f"""INSERT INTO reminders VALUES ("Понедельник", {lesson.name})""")
		cur.commit()
		con.close()