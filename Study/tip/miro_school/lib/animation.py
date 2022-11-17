# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 00:44:53 2022

@author: sujin
"""
import tkinter

WIDTH = 12
HEIGHT = 12

START_POINT = "S"
END_POINT = "E"
WALL = "O"
ROAD = " "


class Animation:
    BLOCK_SIZE = 30
    WALL_SIZE = 30
    END_POINT_SIZE = 30
    CHARACTER_SIZE = 10

    def __init__(self, maze, character_img_path):
        self.tk = tkinter.Tk()
        self.tk.title("미로찾기")
        self.canvas = tkinter.Canvas(width=360, height=360, bg="white")
        self.canvas.pack()
        self.maze = maze
        self.character = tkinter.PhotoImage(file=character_img_path)

    def drawMaze(self):
        map = self.maze
        for y in range(WIDTH):
            for x in range(HEIGHT):
                if map[y][x] == WALL:
                    self.create_wall(x, y)
                elif map[y][x] == END_POINT:
                    self.create_end_point(x, y)
                elif map[y][x] == START_POINT:
                    self.create_character(x, y)
        self.tk.mainloop()
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
        self.canvas.create_image(x * self.BLOCK_SIZE + self.CHARACTER_SIZE,
                                 y * self.BLOCK_SIZE + self.CHARACTER_SIZE,
                                 image=self.character, tag="character")


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

    a = Animation(maze, "NINJA.png")
    a.drawMaze()
