# Carter Esparza
# Assignment 10.1
# 3 December 2021
# In this code I will create my own class to demonstrate knowledge of classes based on a real world object.

import random
import time


class Skateboard:  # Creating a general skateboard class
    num_wheels = 4
    # Adding class variable about the number of wheels on the board
    # Creating the data variables for the skateboard

    def __init__(self, board, wheels, trucks):
        self._board = board
        self._wheels = wheels
        self._trucks = trucks
    # get-sets for each data

    def get_board(self):
        return(self._board)

    def set_board(self, board):
        self._board = board
        return(self._board)

    def get_wheels(self):
        return(self._wheels)

    def set_wheels(self, wheels):
        self._wheels = wheels
        return(self._wheels)

    def get_trucks(self):
        return(self._trucks)

    def set_trucks(self, trucks):
        self._trucks = trucks
        return(self._trucks)

    def do_a_trick(self, confidence, trick):
        # If you're just the right amount of confident, you can do a trick with this
        if confidence > 10:
            print(f"Too confident! {trick} failed!")
            return False
        elif confidence < 0:
            print("Come on! You got this!")
            return False
        elif confidence > random.randrange(0, 10):
            print(f"Dang! Awesome {trick}!")
            return True
        else:
            print(f"Keep practicing your {trick}!")
            return False

    def pop(self, strength):
        # Creates a mini timer that times your ollie based on the strength of the pop
        air_time = int(strength / 3)
        for i in range(air_time):
            print(f"You've spent {air_time - i} seconds in the air!")
            time.sleep(1)
        if air_time > 6:
            response = "Woah you're crazy good!"
        elif air_time >= 1:
            response = "Nice Ollie!"
        else:
            response = "Keep working on your ollie!"
        return response

    def list_setup(self):
        # Creates a list given the makeup of the board from the beginning data variables
        list = f"Board: {self.get_board()}, Wheels: {self.get_wheels()}, Trucks: {self.get_trucks()}"
        return list


def main():
    # I used to skate a Krooked board until it started chipping too much.
    my_setup = Skateboard("Krooked", "Spitfire", "Ace Af-1")
    # my_setup is an actual model of my skateboard. it uses the general class and inputs specific data variables based on my board
    print(Skateboard.list_setup(my_setup))
    new_board = "Quasi"
    # I needed a new deck, however. This is accessing the new board and inputting into my previous setup, replacing the previous board
    my_setup.set_board(new_board)
    print(Skateboard.list_setup(my_setup))
    # With this new board I can do some cool tricks!
    trick1 = "kickflip"
    # this is accessing the do a trick method within the skateboard class
    print(Skateboard.do_a_trick(Skateboard, 6, trick1))
    trick2 = "treflip"
    print(Skateboard.do_a_trick(Skateboard, 2, trick2))
    # I have also been working on my ollies!
    strength1 = 15
    # this is accessing the pop method within the skateboard class
    print(Skateboard.pop(Skateboard, int(strength1)))
    # But dang! I rolled my ankle and feel weak now.
    strength2 = 2
    print(Skateboard.pop(Skateboard, strength2))


if __name__ == "__main__":
    main()
