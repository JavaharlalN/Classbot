from datetime import timedelta as delta
import datetime as dt
from functions import sender

instruction = """Команды
[name] - опциональные параметры
(name/name1/name2) - один из параметров

GET-запросы
?помощь, ?команды - получить список команд
?дз - получить дз на ближайший учебный день
?дз.(завтра/пн/среда/вчера/послезавтра/дд.мм).[предмет] - получить дз на заданный день
?<выражение> - калькулятор
?(пн/среда) - показать расписание на указанный день
?сколько - получить % (без обновления названия беседы)
?анекдот - получить анекдот
?напоминания - показать список напоминаний в формате "текст, день.месяц, минута:час, индекс, повторять (да/нет), периодичность (в днях)"

SET-запросы  
!дз.предмет.день.месяц.задание - записать дз на заданное число
!дз.предмет.задание - установить дз на следующий урок по заданному предмету
!сколько - обновить % (с обновлением названия беседы)
!(игра/громко) - игра
!тихо - закончить игру
!напомнить.текст.день.[месяц].[час].[минута] - напомнить один раз в указанное время. по умолчанию 7 часов 0 минут. Возвращает индекс напоминания.
!напоминать.текст.[час].[минута].[период] - напоминать каждый день (зависит от периода: 1 - повторять каждый день; 2 - повторять каждые два дня, т.е. через день и т.д.). По умолчанию - напоминать раз в день в 7 часов 0 минут. Возвращает индекс напоминания.
!удалить.[индекс] - удалить напоминание. Если не указать индекс, удалит последнее
!формат.<формат> - установить формат показа напоминаний (для !напоминания)
"""

weekdays = {
	"пн": 0,
	"вт": 1,
	"ср": 2,
	"чт": 3,
	"пт": 4,
	"сб": 5,
	"понедельник": 0,
	"вторник":     1,
	"среда":       2,
	"четверг":     3,
	"пятница":     4,
	"суббота":     5,
}


def help(chat_id):
	sender(chat_id, instruction)


def persentage(chat_id):
	hm = (dt.datetime.now() - dt.datetime(2021, 9, 1)).total_seconds() / 31536000
	if hm >= 1:
		sender(chat_id, "Ну вот и всё, прощай лето... 100%")
	else:
		sender(chat_id, str(hm * 100) + '%')


def nearest_hw(chat_id, timetable):
	timetable.update()
	hw = timetable.nearest_hw()
	if hw:
		sender(chat_id, "\n".join(f"{t[0]}, {t[1]}" for t in hw))


def homework(chat_id, timetable, parameters):
	date = dt.date.today()
	if len(parameters) in (1, 2):
		if parameters[0] == "завтра":
			hw = timetable.hw_to_date(date + delta(1))
		elif parameters[0] == "послезавтра":
			hw = timetable.hw_to_date(date + delta(2))
		elif parameters[0] == "вчера":
			hw = timetable.hw_to_date(date + delta(-1))
		elif parameters[0] == "позавчера":
			hw = timetable.hw_to_date(date + delta(-2))
		elif parameters[0] in weekdays:
			diff = weekdays[parameters[0]] - date.weekday()  # need - today
			if diff > 0:
				hw = timetable.hw_to_date(date + delta(diff))
			else:
				hw = timetable.hw_to_date(date + delta(7 + diff))
		elif parameters[0].isdigit() and parameters[1].isdigit():
			d = parameters[0]
			m = parameters[1]
			date_need = dt.datetime(date.year + (1 if m < 6 else 0), m, d)
			sender(chat_id, timetable.hw_to_date(date + (date - date_need).days))
			return
		else:
			sender(chat_id, "не понял")
			return
		if len(parameters) == 2:
			hw = timetable.select(parameters[1], hw)
	elif len(parameters) == 3 and parameters[0].isdigit() and parameters[1].isdigit():
		d = parameters[0]
		m = parameters[1]
		date_need = dt.datetime(date.year + (1 if m < 6 else 0), m, d)
		h = timetable.hw_to_date(date + (date - date_need).days);
		sender(chat_id, timetable.select(parameters[2], h))
		return
	else:
		sender(chat_id, "слишком много параметров")
		return
	if hw:
		sender(chat_id, "\n".join(map(lambda t: f"{t[0]}, {t[1]}", hw)))
	else:
		sender(chat_id, "не задано")


def reminders(chat_id, reminders):
	rs = reminders.get()
	if rs:
		sender(chat_id, '\n'.join(rs))
	else:
		sender(chat_id, "не найдено")


def timetable(chat_id, weekday, timetable):
	sender(chat_id, timetable.get_tt_by_id(weekday))
