import matplotlib.pyplot as plt

from board import Board
from knight import Knight


class TKJ:
    def __init__(self) -> None:
        self.board = Board()
        self.knight = Knight()


    def traverse_board(self):
        next_square = tuple(self.knight.find_next_square(self.board))
        self.board.grid[next_square] *= -1
        self.knight.move(next_square)


    def plot_sim(self):
        self.knight.show() # maybe at the point, just print the number here
        plt.show()

if __name__ == "__main__":
    tkj = TKJ()

    for _ in range(0, 2015):
        tkj.traverse_board()
    

    tkj.plot_sim()
