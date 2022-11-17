# 길내고 기둥넣기 완성
import random

WIDTH = 12
HEIGHT = 12

START_POINT = "S"
END_POINT = "E"
WALL = "O"
ROAD = " "

RIGHT = 0
DOWN = 2


class Maze:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.wall_cnt = 30  # self.wall_cnt = random.randrange(10, 30)
        self.map = [[WALL for col in range(self.width)] for row in range(self.height)]
        self.createMap()

    def createMap(self):
        x, y = 1, 1

        # 시작점 표시
        self.map[x][y] = START_POINT

        while True:  # x 또는 y 좌표가 맨 끝 지점일 때 까지 움직인다.
            # 길을 생성할 방향지정
            direction = random.randrange(RIGHT, DOWN)
            if direction == RIGHT:
                x = x + 1
            else:
                y = y + 1

            self.map[y][x] = ROAD

            # 길의 종료 및 목적지 표시
            if x == 10 or y == 10:  # x 또는 y 의 끝부분까지 이동하여 그곳에 도착지를 만듦
                self.map[y][x] = END_POINT
                break

        # 벽 갯수를 확인하 목표에 맞게 수정한다.
        cnt = 0
        print("목표 벽 갯수 : ", self.wall_cnt)
        # self.printMap()

        for row in range(1, 11):
            for col in range(1, 11):
                if self.map[row][col] == WALL:
                    cnt = cnt + 1
        print("현재 벽 갯수 : ", cnt)

        '''
        while self.wall_cnt > cnt:
            x = random.randrange(1, 11)
            y = random.randrange(1, 11)

            if self.map[y][x] == ROAD:
                self.map[y][x] = WALL
                cnt = cnt + 1
        print("현재 벽 갯수 : ", cnt)
        '''

        while self.wall_cnt < cnt:
            x = random.randrange(1, 11)
            y = random.randrange(1, 11)

            if self.map[y][x] == WALL:
                self.map[y][x] = ROAD
                cnt = cnt - 1
        print("현재 벽 갯수 : ", cnt)

    def printMap(self):
        print("\n[MAP]")
        for row in range(self.height):
            for col in range(self.width):
                print(self.map[row][col], end=' ')
            print()

    def getMap(self):
        return self.map


if __name__ == '__main__':
    m = Maze()
    # m.printMap()
    map = m.getMap()
    print(map)
