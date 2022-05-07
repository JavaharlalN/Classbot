import datetime

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

SET-запросы  
!дз.предмет.день.месяц.задание - записать дз на заданное число
!дз.предмет.задание - установить дз на следующий урок по заданному предмету
!сколько - обновить % (с обновлением названия беседы)
!(игра/громко) - игра
!тихо - закончить игру
!напомнить.текст.день.[месяц].[час].[минута] - напомнить один раз в указанное время. по умолчанию 7 часов 0 минут. Возвращает индекс напоминания.
!напоминать.текст.[час].[минута].[период] - напоминать каждый день (зависит от периода: 1 - повторять каждый день; 2 - повторять каждые два дня, т.е. через день и т.д.). По умолчанию - напоминать раз в день в 7 часов 0 минут. Возвращает индекс напоминания.
!удалить.[индекс] - удалить напоминание. Если не указать индекс, удалит последнее
!напоминания - показать список напоминаний в формате "текст, день.месяц, минута:час, индекс, повторять (да/нет), периодичность (в днях)"
!формат.<формат> - установить формат показа напоминаний (для !напоминания)
"""


def help(chat_id):
	sender(chat_id, instruction)


def persentage(chat_id):
	hm = (datetime.datetime.now() - datetime.datetime(2021, 9, 1)).total_seconds() / 31536000
	if hm >= 1:
		sender(chat_id, "Ну вот и всё, прощай лето... 100%")
	else:
		sender(chat_id, str(hm * 100) + '%')