import sqlite3
from datetime import datetime, timedelta as delta


class Lesson:
	def __init__(self, name, start):
		self.name = name
		self.start = start
		self.homework = ""

	def end(self):
		h = self.start[0] + self.start[1] // 60  # hours
		m = self.start[1] % 60  # minutes
		return (h, m)

	def as_tuple(self):
		return (self.name, self.homework)


class Timetable:
	def __init__(self):
		self.monday = [
			Lesson("История", (8, 30)),
			Lesson("История", (9, 20)),
			Lesson("Физика", (10, 10)),
			Lesson("Физика", (11, 0)),
			Lesson("Информатика, первая группа", (12, 40)),
			Lesson("Английский, вторая группа", (12, 40)),
			Lesson("Информатика, первая группа", (13, 30)),
			Lesson("Английский, вторая группа", (13, 30)),
		]
		self.tuesday = [
			Lesson("Алгебра", (8, 30)),
			Lesson("Алгебра", (9, 20)),
			Lesson("Английский, первая группа", (10, 10)),
			Lesson("Информатика, вторая группа", (10, 10)),
			Lesson("Английский, первая группа", (11, 0)),
			Lesson("Информатика, вторая группа", (11, 0)),
			Lesson("Физика", (12, 40)),
			Lesson("Физика", (13, 30)),
			Lesson("ОБЖ", (14, 20)),
		]
		self.wednesday = [
			Lesson("Русский", (8, 30)),
			Lesson("Русский", (9, 20)),
			Lesson("Физика", (10, 10)),
			Lesson("Физика", (11, 0)),
			Lesson("Индивидуальный проект", (12, 40)),
			Lesson("Индивидуальный проект", (13, 30)),
			Lesson("История", (14, 20)),
		]
		self.thursday = [
			Lesson("Алгебра", (8, 30)),
			Lesson("Алгебра", (9, 20)),
			Lesson("Геометрия", (10, 10)),
			Lesson("Геометрия", (11, 0)),
			Lesson("Английский, первая группа", (12, 40)),
			Lesson("Информатика, вторая группа", (12, 40)),
			Lesson("Английский, вторая группа", (13, 30)),
			Lesson("Информатика, первая группа", (13, 30)),
		]
		self.friday = [
			Lesson("Физра", (8, 30)),
			Lesson("Физра", (9, 20)),
			Lesson("Литература", (10, 10)),
			Lesson("Литература", (11, 0)),
			Lesson("Практикум по физике", (12, 40)),
			Lesson("Практикум по информатике", (13, 30)),
			Lesson("Практикум по математике", (14, 20)),
		]
		self.saturday = []
		self.hemework = []  # tuple(Lesson, datetime.strptime(%d-%m-%Y))

	def save(self):
		con = sqlite3.connect("data.db")
		cur = con.cursor()
		cur.execute("TRUNCATE TABLE IF EXIST timetable")
		cur.execute("TRUNCATE TABLE IF EXIST homework")
		cur.execute(f"""CREATE TABLE IF NOT EXIST timetable
							(day text, lesson text)""")
		cur.execute(f"""CREATE TABLE IF NOT EXIST homework
							(lesson text, task text, date text)""")
		cur.commit()
		for lesson in self.monday:
			cur.execute(f"""INSERT INTO timetable VALUES ("Понедельник", {lesson.name})""")
		for lesson in self.tuesday:
			cur.execute(f"""INSERT INTO timetable VALUES ("Вторник", {lesson.name})""")
		for lesson in self.wednesday:
			cur.execute(f"""INSERT INTO timetable VALUES ("Среда", {lesson.name})""")
		for lesson in self.thursday:
			cur.execute(f"""INSERT INTO timetable VALUES ("Четверг", {lesson.name})""")
		for lesson in self.friday:
			cur.execute(f"""INSERT INTO timetable VALUES ("Пятница", {lesson.name})""")
		for lesson in self.saturdey:
			cur.execute(f"""INSERT INTO timetable VALUES ("Суббота", {lesson.name})""")
		for task in self.homework:
			cur.execute(f"""INSERT INTO homework VALUES
								({task[0].name}, {task[0].homework}, {task[1].strftime("%d-%m-%Y")})""")
		cur.commit()
		con.close()

	def update(self):
		pass

	def when(self):
		weekday = datetime.now().weekday()
		if weekday == 0:
			return self.monday[-1].end() if self.monday else (0, 0)
		if weekday == 1:
			return self.tuesday[-1].end() if self.tuesday else (0, 0)
		if weekday == 2:
			return self.wednesday[-1].end() if self.wednesday else (0, 0)
		if weekday == 3:
			return self.thursday[-1].end() if self.thursday else (0, 0)
		if weekday == 4:
			return self.friday[-1].end() if self.friday else (0, 0)
		if weekday == 5:
			return self.saturday[-1].end() if self.saturday else (0, 0)
		return (0, 0)

	def hw_to_date(self, date):
		tasks = []
		for task in self.hemework:
			if date < task[1] < date + delta(1):
				tasks.append(task[0].as_tuple())
		return tasks
		

	def nearest_hw(self):
		now = datetime.now()
		end = self.when()
		if now.hour > end[0] and now.minute > end[1]:
			return self.hw_to_date(datetime(now.year, now.month, now.day) + delta(1))

	def select(self, lesson, homework):
		[t[0].as_tuple() for t in homework if t[0].name == lesson]
