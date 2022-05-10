from datetime import datetime, time
import sqlite3


class Reminders:
	def __init__(self):
		self.reminders = []  # tuple(value, (day, month), id, (hour, minute))
		self.periodic = []  # tuple(value, period, id, (hour, minute))

	def save(self):
		con = sqlite3.connect("data.db")
		cur = con.cursor()
		cur.execute("TRUNCATE TABLE IF EXIST reminders")
		cur.execute("TRUNCATE TABLE IF EXIST periodic")
		cur.execute(f"""CREATE TABLE IF NOT EXIST reminders
							(value text, rid int, date text, time text)""")
		cur.execute(f"""CREATE TABLE IF NOT EXIST periodic
							(value text, rid int, time text, period int)""")
		con.commit()
		for r in self.reminders:
			dt = datetime(2000, r[1][1], r[1][0], r[3][0], r[3][1])
			df = datetime.strftime(dt, "%d/%m")
			tf = datetime.strftime(dt, "%H.%M")
			cur.execute(f"""INSERT INTO reminders VALUES ({r[0]}, {r[2]}, {df}, {tf})""")
		for r in self.periodic:
			tf = datetime.strftime(time(r[3][0], r[3][1]), "%H.%M")
			cur.execute(f"INSERT INTO periodic VALUES ({r[0]}, {r[2]}, {tf}, {r[1]})")
		con.commit()
		con.close()

	def add(self, value, time=(7, 0), period=None, date=None):
		if not value:
			return "не понял"
		if period is None:
			self.reminders.append((value, date, len(self.reminders), time))
			return f"напоминание с индексом 0-{len(self.reminders) - 1} создано"
		self.periodic.append((value, period, len(self.periodic), time))
		return f"напоминание с индексом 1-{len(self.periodic) - 1} создано"

	def update(self):
		pass

	def get(self):
		reminders = []
		for r in self.reminders:
			d = f"{str(r[1][0]).rjust(2)}.{str(r[1][1]).rjust(2)}"
			t = f"{str(r[3][0]).rjust(2)}:{str(r[3][1]).rjust(2)}"
			reminders.append(f"\"{r[0]}\" {d} {t} {r[2]}")
		for r in self.periodic:
			t = f"{str(r[3][0]).rjust(2)}:{str(r[3][1]).rjust(2)}"
			reminders.append(f"\"{r[0]}\" {t} {r[1]} д. {r[2]}")
		return reminders
