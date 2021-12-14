#!/usr/bin/python3

import numpy as np

input_real_data_path = "real_data.txt"
input_test_data_path = "test_data.txt"

class Board:
    def __init__(self, layout):
        self.layout = np.array(layout)
        self.state = np.zeros_like(self.layout)
        self.won = False

    def proccess_number(self, num):
        if not self.won:
            _state = np.where(self.layout == num, True, False)
            #combine this state with board state
            self.state = np.where(self.state | _state, True, False)
            return self.check_win()
        else:
            return False

    def check_win(self):
        def check_straight(grid):
            for row in grid:
                if False not in row:
                    self.won = True
        # Check rows
        check_straight(self.state)
        # Check cols
        check_straight(np.rot90(self.state))

        return self.won

    def calculate_sum(self):
        sum = np.sum(np.multiply(self.layout, np.invert(self.state)))
        return sum

def import_data(inputFile):
    with open(inputFile, "r") as input_file:
        input_data = input_file.readlines()
    
    drawn = [int(x) for x in input_data[0].rstrip().split(",")]
    input_data.pop(0)

    boards = []
    buffer = []
    for line in input_data:
        line = line.rstrip().split()
        if len(line) > 0:
            buffer.append([int(x) for x in line])

        if len(buffer) == 5:
            boards.append(Board(buffer))
            buffer = []
            
    return drawn, boards

drwan, boards = import_data(input_real_data_path)

for num in drwan:
    print(num)
    for board in boards:
        win = board.proccess_number(num)
        if win:
            print("Winnder", num, "Score:", board.calculate_sum()*num)