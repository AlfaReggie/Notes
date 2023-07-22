import os, csv
from .noteClass import Note

class NotesBook:

    def __init__(self, name: str = "notes.csv", notes_list: list = None):
        if notes_list is None:
            notes_list = []
        self.name = name
        self.notes_list = notes_list

    def add_note(self, note: Note):
        self.notes_list.append(note)

    def remove_note(self, note: Note):
        self.notes_list.remove(note)

    def get_note(self, path):
        note_list = []
        with open(path, 'r', encoding='utf8') as notes_data:
            for note in notes_data:
                note = note.strip().split(';')
                note_list.append(note)
        return note_list

    def __str__(self):
        result_str = f"\nNotes book: "
        if self.notes_list == []:
            return "Notes is empty..."
        for i, note in enumerate(self.notes_list):
            result_str += f"\n{i + 1}: Title: {note.title}\n" \
                          f"Body: {note.body}\n"
        return result_str

    def createFileCsv(self, path, note_info):
        a = ['Id', 'Title', 'Body', 'Time']
        with open(path, 'a', newline='') as state_file:
            writer = csv.DictWriter(state_file, a, delimiter=';')
            writer.writerows(note_info)
