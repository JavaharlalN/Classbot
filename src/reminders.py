from datetime import datetime, time
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
		for r in self.reminders:
			dt = datetime(2000, r[1][1], r[1][0], r[3][0], r[3][1])
			df = datetime.strftime(dt, "%d/%m")
			tf = datetime.strftime(dt, "%H.%M")
			cur.execute(f"""INSERT INTO reminders VALUES ({r[0]}, {df}, {tf})""")
		for r in self.periodic:
			tf = datetime.strftime(time(r[2][0], r[2][1]), "%H.%M")
			cur.execute(f"INSERT INTO periodic VALUES ({r[0]}, {tf})")
		cur.commit()
		con.close()