class Checking:

    def __init__(self, val: list):
        self.val = val

    def check_str(self, numVal: int):
        checkNum = input(f"Enter {self.val[numVal]}: ")
        if checkNum.replace("-", '').isalpha():
            return checkNum
        else:
            print("Error!")
            return Checking.check_str(self, numVal)

    def check_int(self, numbStrVal: int):
        checkNum = input(f"\nEnter {self.val[numbStrVal]}: ")
        if checkNum.replace("-", '').isdigit():
            if int(checkNum) <= 0:
                print("Error! Can't negative!")
                return Checking.check_int(self, numbStrVal)
            return int(checkNum)
        else:
            print("Error!")
            return Checking.check_int(self, numbStrVal)
