import matplotlib.pyplot as plt
import numpy as np

class Board:
    def __init__(self) -> None:
        self.grid = {}
        self.generate_board()

    def generate_board(self):
        square_length = 1
        dir = [0, 1]
        current_square = [0, 0]
        current_value = 0


        for _ in range(0, 1_000):
            for _ in range(0, 2):
                for _ in range(0, square_length):
                    self.grid[tuple(current_square)] = current_value
                    current_square = [sum(i) for i in zip(current_square, dir)]
                    current_value += 1
                dir = self.rotate_90(dir)
            square_length += 1


    # multiply the X part of the vector by -1, and then swap X and Y values
    def rotate_90(self, vect):
        new_y = vect[0]
        vect[0] = vect[1] * -1
        vect[1] = new_y
        return vect


    def show(self):
        for key, value in self.grid.items():
            plt.text(key[0], key[1], str(value))

