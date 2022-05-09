# Команды  
[`name`] - опциональные параметры  
(`name`/`name1`/`name2`) - один из параметров  

## GET  
?`помощь`, ?`команды` - получить список команд  
?`дз` - получить дз на ближайший учебный день  
?`дз`.(`завтра`/`пн`/`среда`/`вчера`/`послезавтра`/`дд.мм`).[`предмет`] - получить дз на заданный день  
Ввод: ?`дз`.`20.02`  
Вывод:
```note
История: прочитать 65536 параграфов
Физика: расщепить атом цезия при помощи зубочистки и пакетика от кошачьего корма
Информатика: взломать базу данных Aliexpress и заполнить задачами про камни
ОБЖ: дожить до завтра
```
?`выражение` - калькулятор  
Ввод: ?`543/0`  
Вывод:
```note
деление на ноль страшное, гроб, гроб, кладбище...
```
?(`пн`/`среда`) - показать расписание на `день`  
?`сколько` - получить % (без обновления названия беседы)  
?`анекдот` - получить анекдот  
?`напоминания` - показать список напоминаний  

## SET  
!`дз`.`предмет`.`день`.`месяц`.`задание` - установить дз на заданное число  
!`дз`.`предмет`.`задание` - установить дз на следующий урок по заданному предмету  
!`сколько` - обновить % (с обновлением названия беседы)  
!`игра` - игра  
!`тихо` - закончить игру  
!`напомнить`.`текст`.`день`.[`месяц`].[`час`].[`минута`] - напомнить один раз в указанное время. по умолчанию 7 часов 0 минут. Возвращает индекс напоминания
!`напоминать`.`текст`.[`час`].[`минута`].[`период`] - напоминать каждый день (зависит от периода: 1 - повторять каждый день; 2 - повторять каждые два дня, т.е. через день и т.д.). По умолчанию - напоминать раз в день в 7 часов 0 минут. Возвращает индекс напоминания  
!`удалить`.[`индекс`] - удалить напоминание. Если не указать индекс, удалит последнее  
Формат напоминаний: `<текст> <дд/мм> <индекс> <чч.мм>`  
Формат периодических напоминаний: `<текст> <индекс> <чч.мм>`  
Пример напоминаний:  
```note
"Скинуться по 50 камней до среды" 14/03 3 08.30
"Обновить список дежурств" 512 03.30
```
!`название` `<формат>`
Пример:
```note
!название С̖̻̣̘̦̤̬̼̪͂̇̍̕͝тальное M̖̻̣̘̦̤̬̼̪͂̇̍̕͝ыло №10.{}
```
