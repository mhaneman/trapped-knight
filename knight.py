from typing import Dict, Optional

class Knight:

    def __init__(self, start_pos: tuple = (0,0)) -> None:
        self.curr_pos = start_pos
        self.move_offsets = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        self.pos_history = []


class NKnight(Knight):
    def __init__(self, n=0, start_pos: tuple = (0,0)) -> None:
        Knight.__init__(self, start_pos)
        self.n = n

    def find_next_square(self, coord_vals: Dict[tuple, int])-> Optional[tuple]:
        visited = []
        
        for offset in self.move_offsets:
            pot_pos = tuple(map(lambda i, j: i + j, offset, self.curr_pos))
            pot_val = coord_vals[pot_pos]

            if pot_val > 0:
                visited.append((pot_pos, pot_val))

        if len(visited) == 0:
            return None

        visited.sort(reverse=True, key=lambda e: e[1])

        for _ in range(self.n):
            if (len(visited) == 1):
                break
            visited.pop()

        result = visited.pop()[0]
        self.curr_pos = result
        self.pos_history.append(result)
        return result
