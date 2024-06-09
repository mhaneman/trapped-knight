import matplotlib.pyplot as plt

import matplotlib.animation as animation

from board import Board
from knight import NKnight

class Simulation:

    def __init__(self, knight, board, steps) -> None:
        self.steps = steps
        self.board = board 
        self.knight = knight 


    def calc_move(self) -> bool:
        next_pos = self.knight.find_next_square(self.board.coord_vals)
        
        if next_pos is None:
            return False

        self.board.coord_vals[next_pos] *= -1 # update board
        return True


    def run(self):
        self.board.coord_vals[(0, 0)] *= -1 # update board

        for step in range(self.steps):
            if self.calc_move() is False:
                print("STUCK! at: ", self.knight.curr_pos, " at step: ", step+1)
                break


    def static_graph(self):
        self.__graph_knight_history()
        self.__graph_board_vals()
        
        plt.xlim([-10, 10])
        plt.ylim([-10, 10])
        plt.show()

    def __graph_knight_history(self):
        plt.plot(*zip(*self.knight.pos_history), color="gray")
        x, y = self.knight.curr_pos[0], self.knight.curr_pos[1]
        plt.plot(x, y, marker="o", markeredgecolor="red", markersize=5, markerfacecolor="red")


    def __graph_board_vals(self):
        i = 0
        for key, val in self.board.coord_vals.items():
            if i < 100:
                plt.text(key[0], key[1], str(val))
                i += 1
            else:
                break

    def animate_graph(self):

        fig, ax = plt.subplots()
        x0, y0 = self.knight.pos_history[0]
        line = ax.plot(x0, y0)[0]

        def update(frame):
            xs = [x[0] for x in self.knight.pos_history[:frame]]
            ys = [x[1] for x in self.knight.pos_history[:frame]]
            line.set_xdata(xs)
            line.set_ydata(ys)

            if frame > 0:
                ax.set_xlim(min(-10, min(xs)), max(10, max(xs)))
                ax.set_ylim(min(-10, min(ys)), max(10, max(ys)))

            return line


        if len(self.board.prime_squares) > 0:
            ax.scatter(*zip(*self.board.prime_squares), color="red", s=1)

        ax.plot(self.knight.curr_pos[0], self.knight.curr_pos[1], 'go', markersize=1) 
        
        anim = animation.FuncAnimation(fig=fig, func=update, frames=self.steps, interval=30)
        
        # writervideo = animation.FFMpegWriter(fps=60) 
        # anim.save('std.mp4', writer=writervideo) 
        plt.show()
        # plt.close()




if __name__ == "__main__":
    knight = NKnight(start_pos=(0, 0), n=0)
    board = Board(spiral_size=1000, negate_primes=False)

    sim = Simulation(knight=knight, board=board, steps=2200)

    sim.run()
    sim.animate_graph()
    

