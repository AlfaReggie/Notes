from .notesBook import NotesBook
from .noteClass import Note
from .commands import Commands
from .checking import Checking
from datetime import datetime

class Travel:

    def __init__(self, PATH_NAME, commands_list: list, question_list: list):
        self.path = PATH_NAME
        self.commands_list = commands_list
        self.quest_list = question_list

    def start_menu(self, exit: bool):
        if exit == True:
            print('Ok! Bye =)')
        else:
            print("Start program...\n")
            self.menu_dir()

    def menu_dir(self):
        self.book_list = NotesBook()
        self.book_list.get_note(self.path)
        commands = Commands(self.commands_list[0])
        print(commands)
        checking = Checking(self.quest_list)
        answ = False
        while answ == False:
            answ = commands.check_command(checking.check_int(4))
        if answ == 1:
            self.menu_lib()
        elif answ == 2:
            self.start_menu(True)

    def menu_lib(self):
        for i in range(len(self.book_list.get_note(self.path))):
            print(f'{i + 1}: {self.book_list.get_note(self.path)[i]}')
        commands = Commands(self.commands_list[1])
        print(commands)
        checking = Checking(self.quest_list)
        answ = False
        while answ == False:
            answ = commands.check_command(checking.check_int(4))
        if answ == 1:
            if len(self.book_list.get_note(self.path)) != 0:
                self.menu_update(False)
            else:
                self.menu_update(True)
        elif answ == 2:
            self.menu_dir()

    def menu_update(self, empty: bool):
        if empty == True:
            print(self.book_list)
            commands = Commands(self.commands_list[2])
            self.update_empty(commands)
        else:
            commands = Commands(self.commands_list[3])
            self.update_notes(commands)

    def update_empty(self, commands):
        print(commands)
        checking = Checking(self.quest_list)
        answ = 0
        while answ == False:
            answ = commands.check_command(checking.check_int(4))
        if answ == 1:
            note_title = input("Enter title your note: ")
            note_body = input("Enter text your note: ")
            current_datetime = datetime.now()
            note = Note(note_id=1, note_title=note_title, note_body=note_body, time_of_change=current_datetime)
            self.book_list.add_note(note)
            note_info = [note.get_note()]
            self.book_list.createFileCsv(self.path, note_info, 'a')
            commands = Commands(self.commands_list[3])
            self.update_notes(commands)
        elif answ == 2:
            for i in range(len(self.book_list.get_note(self.path))):
                print(f'{i + 1}: {self.book_list.get_note(self.path)[i]}')
            commands = Commands(self.commands_list[3])
            self.update_notes(commands)
        elif answ == 3:
            self.menu_lib()

    def update_notes(self, commands):
        print(commands)
        checking = Checking(self.quest_list)
        answ = 0
        while answ == False:
            answ = commands.check_command(checking.check_int(4))
        if answ == 1:
            for i in range(1, len(self.book_list.get_note(self.path))):
                if i != len(self.book_list.get_note(self.path)):
                    id = i
            note_title = input("Enter title your note: ")
            note_body = input("Enter text your note: ")
            id = int(self.book_list.get_note(self.path)[-1][0]) + 1
            current_datetime = datetime.now()
            note = Note(note_id=id, note_title=note_title, note_body=note_body, time_of_change=current_datetime)
            self.book_list.add_note(note)
            note_info = [note.get_note()]
            self.book_list.createFileCsv(self.path, note_info, 'a')
            commands = Commands(self.commands_list[3])
            self.update_notes(commands)
        elif answ == 2:
            while True:
                choise_number = commands.check_command(checking.check_int(5)) - 1
                if choise_number <= len(self.book_list.get_note(self.path)) + 1:
                    break
            while True:
                choise = input("Enter 't' for change title info or 'b' for change body info: ")
                if choise == 't':
                    new_info = input("Enter new info: ")
                    notes = []
                    for i in range(len(self.book_list.get_note(self.path))):
                        if i != choise_number:
                            note = self.book_list.get_note(self.path)[i]
                            note = Note(note_id=note[0], note_title=note[1], note_body=note[2],
                                        time_of_change=note[3])
                            self.book_list.add_note(note)
                            note_info = [note.get_note()]
                            notes.append(note_info)
                        else:
                            note = self.book_list.get_note(self.path)[i]
                            note = Note(note_id=note[0], note_title=new_info, note_body=note[2],
                                        time_of_change=note[3])
                            self.book_list.add_note(note)
                            note_info = [note.get_note()]
                            notes.append(note_info)
                    self.book_list.createFileCsv(self.path, '', 'w')
                    for i in notes:
                        self.book_list.createFileCsv(self.path, i, 'a')
                    commands = Commands(self.commands_list[3])
                    self.update_notes(commands)
                elif choise == 'b':
                    new_info = input("Enter new info: ")
                    notes = []
                    for i in range(len(self.book_list.get_note(self.path))):
                        if i != choise_number:
                            note = self.book_list.get_note(self.path)[i]
                            note = Note(note_id=note[0], note_title=note[1], note_body=note[2],
                                        time_of_change=note[3])
                            self.book_list.add_note(note)
                            note_info = [note.get_note()]
                            notes.append(note_info)
                        else:
                            note = self.book_list.get_note(self.path)[i]
                            note = Note(note_id=note[0], note_title=note[1], note_body=new_info,
                                        time_of_change=note[3])
                            self.book_list.add_note(note)
                            note_info = [note.get_note()]
                            notes.append(note_info)
                    self.book_list.createFileCsv(self.path, '', 'w')
                    for i in notes:
                        self.book_list.createFileCsv(self.path, i, 'a')
                    commands = Commands(self.commands_list[3])
                    self.update_notes(commands)
        elif answ == 3:
            while True:
                choise_number = commands.check_command(checking.check_int(5)) - 1
                if choise_number <= len(self.book_list.get_note(self.path)):
                    break
            notes = []
            for i in range(len(self.book_list.get_note(self.path))):
                if i != choise_number:
                    note = self.book_list.get_note(self.path)[i]
                    note = Note(note_id=i+1, note_title=note[1], note_body=note[2],
                                    time_of_change=note[3])
                    self.book_list.add_note(note)
                    note_info = [note.get_note()]
                    notes.append(note_info)
            self.book_list.createFileCsv(self.path, '', 'w')
            for i in notes:
                self.book_list.createFileCsv(self.path, i, 'a')
            commands = Commands(self.commands_list[3])
            self.update_notes(commands)
        elif answ == 4:
            for i in range(len(self.book_list.get_note(self.path))):
                print(f'{i + 1}: {self.book_list.get_note(self.path)[i]}')
            commands = Commands(self.commands_list[3])
            self.update_notes(commands)
        elif answ == 5:
            self.menu_dir()
