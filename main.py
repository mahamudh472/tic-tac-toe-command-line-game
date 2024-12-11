
"""
###########################################
# Project Name: Tic Tac Toe command line game
# Author: Md Mahmud Hasan
# Email: mahadymahamudh472@gmail.com
# GitHub: https://github.com/mahamudh472
# Description: This game is only a command line game. So it will run as a script and displayed in the terminal.
# Created On: 1 Nov 2023
###########################################
"""


import os 

TURN = None     #Blue/Red
BLUE_TEAM_SIGN = "O"
RED_TEAM_SIGN = "X"
WIN = None      #Blue/Red/None

class Board:
    def __init__(self) -> None:
        self.row1_col1 = " "
        self.row1_col2 = " "
        self.row1_col3 = " "
        self.row2_col1 = " "
        self.row2_col2 = " "
        self.row2_col3 = " "
        self.row3_col1 = " "
        self.row3_col2 = " "
        self.row3_col3 = " "

    def renderBoard(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f" {self.row1_col1} | {self.row1_col2} | {self.row1_col3}")
        print(f"----------")
        print(f" {self.row2_col1} | {self.row2_col2} | {self.row2_col3}")
        print("----------")
        print(f" {self.row3_col1} | {self.row3_col2} | {self.row3_col3}")

    def alreadyTakenError(self):
        print("Field is already taken")
        self.update_board()
        return

    def update_board(self):
        print(f"Turn: {TURN}")
        inp = input("Enter your move: ")
        if inp == "1":
            if self.row1_col1 != " ":
                self.alreadyTakenError()
            else:
                self.row1_col1 = TURN
        elif inp == "2":
            if self.row1_col2 != " ":
                self.alreadyTakenError()
            else:
                self.row1_col2 = TURN
        elif inp == "3":
            if self.row1_col3 != " ":
                self.alreadyTakenError()
            else:
                self.row1_col3 = TURN
        elif inp == "4":
            if self.row2_col1 != " ":
                self.alreadyTakenError()
            else:
                self.row2_col1 = TURN
        elif inp == "5":
            if self.row2_col2 != " ":
                self.alreadyTakenError()
            else:
                self.row2_col2 = TURN
        elif inp == "6":
            if self.row2_col3 != " ":
                self.alreadyTakenError()
            else:
                self.row2_col3 = TURN
        elif inp == "7":
            if self.row3_col1 != " ":
                self.alreadyTakenError()
            else:
                self.row3_col1 = TURN
        elif inp == "8":
            if self.row3_col2 != " ":
                self.alreadyTakenError()
            else:
                self.row3_col2 = TURN
        elif inp == "9":
            if self.row3_col3 != " ":
                self.alreadyTakenError()
            else:
                self.row3_col3 = TURN
        else:
            print("Invalid input")
            self.update_board()
            
        
    def start(self):
        global TURN, WIN
        TURN = BLUE_TEAM_SIGN
        print("Welcome to Tic Tac Toe!")

        self.renderBoard()
        while WIN==None:
            self.update_board()
            self.renderBoard()
            self.check_win()
            if TURN == BLUE_TEAM_SIGN:
                TURN = RED_TEAM_SIGN
            else:
                TURN = BLUE_TEAM_SIGN

    def check_win(self):
        global WIN
        # if all positions are fill and no one wins:
        if self.row1_col1 != " " and self.row1_col2 != " " and self.row1_col3 != " " and self.row2_col1 != " " and self.row2_col2 != " " and self.row2_col3 != " " and self.row3_col1 != " " and self.row3_col2 != " " and self.row3_col3 != " ":
            WIN = "None"
            print("No one wins")
            return
        if self.row1_col1 == self.row1_col2 == self.row1_col3 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row2_col1 == self.row2_col2 == self.row2_col3 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row3_col1 == self.row3_col2 == self.row3_col3 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row1_col1 == self.row2_col1 == self.row3_col1 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row1_col2 == self.row2_col2 == self.row3_col2 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row1_col3 == self.row2_col3 == self.row3_col3 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row1_col1 == self.row2_col2 == self.row3_col3 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row1_col3 == self.row2_col2 == self.row3_col1 == BLUE_TEAM_SIGN:
            WIN = BLUE_TEAM_SIGN
            print(f"{BLUE_TEAM_SIGN} team wins!")
        elif self.row1_col1 == self.row1_col2 == self.row1_col3 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row2_col1 == self.row2_col2 == self.row2_col3 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row3_col1 == self.row3_col2 == self.row3_col3 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row1_col1 == self.row2_col1 == self.row3_col1 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row1_col2 == self.row2_col2 == self.row3_col2 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row1_col3 == self.row2_col3 == self.row3_col3 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row1_col1 == self.row2_col2 == self.row3_col3 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        elif self.row1_col3 == self.row2_col2 == self.row3_col1 == RED_TEAM_SIGN:
            WIN = RED_TEAM_SIGN
            print(f"{RED_TEAM_SIGN} team wins!")
        else:
            WIN = None
            print("No one wins")

if __name__ == "__main__":
    my_bord = Board()
    my_bord.start()