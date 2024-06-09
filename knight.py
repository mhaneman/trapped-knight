import matplotlib.pyplot as plt

class Knight:
    def __init__(self) -> None:
        self.position_history = [(0, 0)]
        self.stuck_positions = []
        
        self.position = [0, 0]
        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


    def move(self, pos):
        self.position = pos


    def find_next_square(self, board):
        priority_moves = []

        for move in self.moves:
            pos = [sum(i) for i in zip(self.position, move)] # update position based on move offset
            val = board.grid[tuple(pos)] # get value of next position_history

            if val > 0:
                priority_moves.append(tuple([pos, val]))

        priority_moves.sort(reverse=True, key=lambda e: e[1])
        
        p = 0
        while(len(priority_moves) > 1 and p > 0):
            priority_moves.pop()
            p -= 1

        result = tuple(priority_moves.pop()[0])
        self.position_history.append(result)
        return result
    

    def show(self):
        plt.plot(*zip(*self.position_history), color="gray")
        x, y = self.position_history[-1]
        plt.plot(x, y, marker="o", markersize=5, markerfacecolor="green")

        for i in self.stuck_positions:
            plt.plot(i[0], i[1], marker="o", markeredgecolor="red", markersize=5, markerfacecolor="red")
            
