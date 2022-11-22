import pygame as game
import numpy as np
import copy


class Cell:
    def __init__(self, id, r, g, b, temp):
        self.id = id
        self.r = r
        self.g = g
        self.b = b
        self.temp = temp

    def get_id(self):
        return self.id

    def get_r(self):
        return self.r

    def get_g(self):
        return self.g

    def get_b(self):
        return self.b

    def get_temp(self):
        return self.temp

    def set_age(self, x):
        self.id = x

    def set_r(self, x):
        self.r = x

    def set_g(self, x):
        self.g = x

    def set_b(self, x):
        self.b = x

    def set_temp(self, x):
        self.temp = x


AIR = 0
WALL = 1
DOOR = 2
WINDOW = 3
HEAT = 4
ONE_DEGREE = 5

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

width = BLOCK_WIDTH
height = BLOCK_HEIGHT

# grid = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -1],
#         [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
#         [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
#         [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
#         [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
#         [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
#         [-1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, -1]]

# grid2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 1, 1, 4, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1]]

grid = [[Cell(1, 0, 0, 0, 0), Cell(1, 0, 0, 0, 0), Cell(1, 0, 0, 0, 0), Cell(1, 0, 0, 0, 0), Cell(1, 0, 0, 0, 0)],
        [Cell(1, 0, 0, 0, 0), Cell(0, 0, 0, 0, 0), Cell(0, 0, 0, 0, 0), Cell(0, 0, 0, 0, 0), Cell(1, 0, 0, 0, 0)],
        [Cell(1, 0, 0, 0, 0), Cell(4, 0, 0, 0, 50), Cell(5, 0, 0, 0, 32), Cell(5, 0, 0, 0, 32), Cell(1, 0, 0, 0, 0)],
        [Cell(1, 0, 0, 0, 0), Cell(1, 0, 0, 0, 11), Cell(1, 0, 0, 0, 0), Cell(3, 0, 0, 0, 0), Cell(1, 0, 0, 0, 0)]]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (142, 60, 60)
BROWN2 = (120, 20, 80)
RED = (255, 20, 20)
HEAT1 = (200, 150, 50)

game.init()

CYCLE = game.USEREVENT + 1
game.time.set_timer(CYCLE, 50)

screen = game.display.set_mode((1000, 500))

clock = game.time.Clock()


def change_state(cur_cell, list_neighbourhood):
    temp1 = list_neighbourhood[0].get_temp()
    temp2 = list_neighbourhood[1].get_temp()
    temp3 = list_neighbourhood[2].get_temp()
    temp4 = list_neighbourhood[3].get_temp()
    updated_cell = copy.deepcopy(cur_cell)
    temp_fin = (temp1 + temp2 + temp3 + temp4) / 4
    updated_cell.set_temp(temp_fin)
    print(updated_cell)
    return updated_cell


def main():
    global grid
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                break
            if event.type == CYCLE:
                gridNew = copy.deepcopy(grid)
                # gridNew = []
                # for row in range(len(grid)):
                #     gridNew.append([])
                #     for column in range(len(grid[0])):
                #         gridNew[row].append(0)

                for row in range(1, len(grid) - 1):
                    for column in range(1, len(grid[0]) - 1):
                        cells = list()
                        if grid[row][column] != 4:
                            cells.append(grid[row + 1][column])
                            cells.append(grid[row - 1][column])
                            cells.append(grid[row][column + 1])
                            cells.append(grid[row][column - 1])
                            gridNew[row][column] = change_state(grid[row][column], cells)
                grid = gridNew

        screen.fill(BLACK)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column].get_id() == 1:
                    color = BROWN
                elif grid[row][column].get_id() == 2:
                    color = BROWN2
                elif grid[row][column].get_id() == 3:
                    color = BLUE
                elif grid[row][column].get_id() == 4:
                    color = RED
                elif grid[row][column].get_temp() > 10:
                    color = HEAT1
                else:
                    color = WHITE
                game.draw.rect(screen, color,
                               [width * column, height * row, width, height])
        game.display.flip()

        clock.tick(1)

    game.quit()


if __name__ == '__main__':
    main()
