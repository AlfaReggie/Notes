import os

PATH_NAME = os.path.join('data', 'notes.csv')

COMMAND_START = ['Open notes book', "Stop program"]
COMMAND_LIBRARY = ["Update file", "Exit to library"]
COMMAND_EMPTY_FILE = ["Add note", "Show notes", 'Exit to files']
COMMAND_FILE = ["Add note", "Update note", 'Delete note', "Show notes", 'Exit to files']

COMMAND_PROGRAM = [COMMAND_START, COMMAND_LIBRARY, COMMAND_EMPTY_FILE, COMMAND_FILE]

LIST_VAL = ["id", "title", "body", "time", "command number", "note number"]
