import os

PATH_NAME = os.path.join('virtualEnv', 'src', 'data', 'notes.csv')
#PATH_NAME = os.path.join('data', 'notes.csv')

COMMAND_START = ['Open notes book(открыть файл заметок)', "Stop program(Завершить программу)"]
COMMAND_LIBRARY = ["Working mode(Режим работы с заметками)",
                   "Exit from library(выход из файла)"]
COMMAND_EMPTY_FILE = ["Add note(добавить заметку)", "Show notes(вывод списка заметок)", 'Exit to files(выйти']
COMMAND_FILE = ["Add note(добавить заметку)", "Update note(редактировать заметку)", 'Delete note(удалить заметку)',
                "Show notes(показать список заметок)", 'Exit to files(выйти из режима)']

COMMAND_PROGRAM = [COMMAND_START, COMMAND_LIBRARY, COMMAND_EMPTY_FILE, COMMAND_FILE]

LIST_VAL = ["id", "title(заголовок)", "body(тело)", "time(время)", "command number(номер команды)", "note number"]
