import os

START_POINT = "S"
END_POINT = "E"
WALL = "O"
ROAD = " "
VISITED = "-"

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class PathFinding:
    foots = [[1,1]]
    allFoots = [[1,1]]
    reverse_foots = []

    def __init__(self, maze, draw_map):
        self.maze = maze
        self.draw_map_bool = draw_map

    def drawMaze(self, maze):  # 미로 시각화
        if (self.draw_map_bool):
            os.system('cls')
            print()
            for y in range(0, len(maze)):
                for x in range(0, len(maze[0])):
                    if (maze[y][x] == WALL):
                        print("■■", end='')
                    elif (maze[y][x] == ROAD):
                        print("%2s" % " ", end='')
                    else:
                        print("%2s" % (maze[y][x]), end='')
                print()

    def goTurtle(self, maze, sx, sy, foots):
        foot = maze[sy][sx]  # 현재 미로 위치
        for di in range(0, 4):  # 4방향 확인
            x = sx + dx[di]
            y = sy + dy[di]
            if (maze[y][x] == END_POINT):  # 도착했을 때 :  x,y 사용자에게 마킹하고 주소 출력
                # maze[y][x] = foot + 1
                foots.append([x, y])
                return True
            if (maze[y][x] == ROAD):  # 가지 않은 곳일 경우 : 마킹 후 다른 길을 다시 탐색
                # maze[y][x] = foot + 1
                maze[y][x] = VISITED
                self.allFoots.append([x, y])
                if self.goTurtle(maze, x, y, foots):
                    foots.append([x, y])
                    return True
        return False

    def findLoad(self, maze, sx, sy):  # 미로 탐색 시작
        self.drawMaze(maze)
        foots = []
        self.goTurtle(maze, sx, sy, foots)
        self.drawMaze(maze)
        foots.reverse()
        self.foots = foots
        return self.getFoots()

    def getFoots(self):
        return self.allFoots
        # return self.foots

    def getReverseFoots(self):
        self.reverse_foots = self.foots.copy()
        self.reverse_foots.reverse()
        self.reverse_foots.append([1,1])
        return self.reverse_foots


if __name__ == '__main__':
    maze = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'S', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', 'O'],
            ['O', ' ', ' ', 'O', 'O', ' ', ' ', 'O', ' ', ' ', 'O', 'O'],
            ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O', 'O', ' ', 'O'],
            ['O', 'O', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
            ['O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', 'E', ' ', 'O'],
            ['O', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' ', 'O'],
            ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            ['O', 'O', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', 'O'],
            ['O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', 'O'],
            ['O', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

    pf = PathFinding(maze, True)
    pf.findLoad(maze, 1, 1)
    print("출발", pf.getFoots())
    print()
    print("도착", pf.getReverseFoots())

    print(maze)
