from pathlib import Path

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def change(self, x, y):
        self.x += x
        self.y += y


class MoveStrategy:
    def __init__(self, move_x, move_y):
       self.position = Position() 
       self.move_x = move_x
       self.move_y = move_y

    def move(self):
        self.position.change(self.move_x, self.move_y)


class Track:
    TREE = '#'

    def __init__(self, grid):
        self._grid = grid
        self.max_x_location = len(self._grid[0]) 
        self.end_y_location = len(self._grid)

    def is_coliding(self, position, obsticle=TREE):
        overload_x = position.x % self.max_x_location
        return self._grid[position.y][overload_x] == obsticle

    def is_in_boundery(self, position):
        return position.y < track.end_y_location


def count_collisions(track, strategy):
    result = 0
    while track.is_in_boundery(strategy.position):
            result += track.is_coliding(strategy.position)
            strategy.move()
    return result


def solution_one(track):
    count_collisions(track, MoveStrategy(3, 1))


def solution_two(track):
    strategies = [
        MoveStrategy(1, 1),
        MoveStrategy(3, 1),
        MoveStrategy(5, 1),
        MoveStrategy(7, 1),
        MoveStrategy(1, 2),
    ]

    result = 1
    for strategy in strategies:
        result *= count_collisions(track, strategy)
    return result


if __name__ == "__main__":
    with Path('input.txt').open() as file_:
        # Clear new lines
        input_ = [line.strip('\n') for line in file_] 

    track = Track(grid=input_)

    solution_one(track)
    solution_two(track)
