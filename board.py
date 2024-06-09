from typing import Dict
import math

class Board:
    def __init__(self, spiral_size=0, negate_primes=False) -> None: 
        self.coord_vals: Dict[tuple, int] = {} 
        self.prime_squares = []
        self.gen_spiral(spiral_size, negate_primes)

    def gen_spiral(self, spiral_size, negate_primes):
        square_length = 1
        dir = [0, 1]
        current_square = [0, 0]
        current_value = 0

        for _ in range(0, spiral_size):
            for _ in range(0, 2):
                for _ in range(0, square_length):
                    if negate_primes and self.is_prime(current_value):
                        self.coord_vals[tuple(current_square)] = -current_value
                        self.prime_squares.append(tuple(current_square))
                    else:
                        self.coord_vals[tuple(current_square)] = current_value

                    current_square = [sum(i) for i in zip(current_square, dir)]
                    current_value += 1
                dir = self.rot_vec2_90(dir)
            square_length += 1


    # to rotate right, multiply the x part of the vector by -1, and then swap X and Y values
    def rot_vec2_90(self, vect):
        new_y = vect[0]
        vect[0] = vect[1] * -1
        vect[1] = new_y
        return vect


    def is_prime(self, n: int) -> bool: 
        # Check if n=1 or n=0 
        if n <= 1: 
            return False
      
        # Check if n=2 or n=3 
        if n == 2 or n == 3: 
            return True
      
        # Check whether n is divisible by 2 or 3 
        if n % 2 == 0 or n % 3 == 0: 
            return False
      
        # Check from 5 to square root of n 
        # Iterate i by (i+6) 
        for i in range(5, int(math.sqrt(n))+1, 6): 
            if n % i == 0 or n % (i + 2) == 0: 
                return False
  
        return True



