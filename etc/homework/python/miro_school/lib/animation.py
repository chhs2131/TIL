# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 15:06:51 2022

@author: sujin
"""

import tkinter
import time

WIDTH = 12
HEIGHT = 12

START_POINT = "S"
END_POINT = "E"
WALL = "O"
ROAD = " "


class Animation:
    maze = []
    now_ch_x = 1
    now_ch_y = 1

    BLOCK_SIZE = 30
    WALL_SIZE = 30
    END_POINT_SIZE = 30
    CHARACTER_SIZE = 10

    def __init__(self, maze):
        self.tk = tkinter.Tk()
        self.tk.title("미로찾기")
        self.canvas = tkinter.Canvas(width=360, height=360, bg="white")
        self.canvas.pack()
        self.setMaze(maze)
        # self.character = tkinter.PhotoImage(file=character_img_path)

    def setMaze(self, maze):
        self.maze = maze

    def setCharacterPos(self, x, y):
        print("==>", x, y, self.now_ch_x, self.now_ch_y)
        self.now_ch_x = x
        self.now_ch_y = y

    def movingRoute(self, path):
        for p in path:  # path => [[y,x] ...]
            x, y = p
            self.moveCharacter(x, y)
            self.drawMaze()

    def moveCharacter(self, x, y):
        print(x, y, "로 이동하자", self.now_ch_x, self.now_ch_y)
        self.create_visited(self.now_ch_x, self.now_ch_y)
        self.create_character(x, y)
        time.sleep(0.1)

    def drawMaze(self):
        map = self.maze
        for y in range(WIDTH):
            for x in range(HEIGHT):
                if map[y][x] == WALL:
                    self.create_wall(x, y)
                elif map[y][x] == END_POINT:
                    self.create_end_point(x, y)
                # elif map[y][x] == START_POINT:
                #     self.create_character(x, y)
            # self.tk.mainloop()
            # self.tk.update_idletasks()
            self.tk.update()
        print(map)

    def create_wall(self, x, y):
        self.canvas.create_rectangle(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE,
                                     x * self.BLOCK_SIZE + self.WALL_SIZE,
                                     y * self.BLOCK_SIZE + self.WALL_SIZE,
                                     fill='blue')

    def create_end_point(self, x, y):
        self.canvas.create_rectangle(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE,
                                     x * self.BLOCK_SIZE + self.END_POINT_SIZE,
                                     y * self.BLOCK_SIZE + self.END_POINT_SIZE,
                                     fill='red')

    def create_character(self, x, y):
        self.setCharacterPos(x, y)
        self.canvas.create_rectangle(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE,
                                     x * self.BLOCK_SIZE + self.END_POINT_SIZE,
                                     y * self.BLOCK_SIZE + self.END_POINT_SIZE,
                                     fill='green')

    def create_visited(self, x, y):
        self.canvas.create_rectangle(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE,
                                     x * self.BLOCK_SIZE + self.END_POINT_SIZE,
                                     y * self.BLOCK_SIZE + self.END_POINT_SIZE,
                                     fill='gray')


if __name__ == '__main__':
    maze = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'S', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', 'O'],
            ['O', ' ', ' ', 'O', 'O', ' ', ' ', 'O', ' ', ' ', 'O', 'O'],
            ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O', 'O', ' ', 'O'],
            ['O', 'O', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
            ['O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            ['O', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' ', 'O'],
            ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'O'],
            ['O', 'O', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', 'O'],
            ['O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', 'O'],
            ['O', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

    print("abcde")
    a = Animation(maze)
    # a.drawMaze()

    print("abcde")
    path = [[2, 1], [2, 2], [2, 3], [3, 3], [4, 3], [5, 3], [5, 4], [6, 4], [7, 4], [8, 4], [8, 5], [9, 5], [10, 5],
            [10, 6], [10, 7]]
    a.movingRoute(path)
    print("abcde")
