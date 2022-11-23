import lib.maze as makemaze
import lib.pathfinding as pathfind
import lib.animation as animation
import time

# 미로 생성
m = makemaze.Maze()
maze = m.getMap()

# 찾기 경로 생성
pf = pathfind.PathFinding(maze, draw_map=False)
pf.findLoad(maze, 1, 1)

path = pf.getFoots()
reverse_path = pf.getReverseFoots()
print("출발", path)
print("도착", reverse_path)

# GUI 생성
gui = animation.Animation(maze)
gui.drawMaze()
gui.movingRoute(path)

gui.movingRoute(reverse_path)
print("미로탐색 완료! 10초후에 종료됩니다.")
time.sleep(10)
