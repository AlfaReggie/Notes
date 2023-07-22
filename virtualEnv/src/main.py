from const import PATH_NAME, COMMAND_PROGRAM, LIST_VAL
from data_worker import Travel

travel = Travel(PATH_NAME, COMMAND_PROGRAM, LIST_VAL)

if __name__ == "__main__":
    travel.start_menu(False)
