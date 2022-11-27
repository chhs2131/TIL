def matrixMult(A):
    row = len(A)
    col = len(A[0])
    B = [[0 for row in range(row)] for col in range(col)]

    for i in range(row):
        for j in range(col):
            B[j][i] = A[i][j]
    return B


# 입력받기
h, w = input().split()
h = int(h)
w = int(w)
filed = []
visited = [[-1 for i in range(w)] for j in range(h)]

for i in range(0, h):
    filed.append(list(input()))


# 구름이 점점 한칸씩 밀려난다!
dot_filed = ['.' for i in range(h)]
for turn in range(0, w):
    # 해당칸을 확인
    for i in range(0, h):
        for j in range(0, w):
            # 아직 방문하지 않은 곳이고
            if visited[i][j] == -1:
                # 현재 구름이 있다면
                if filed[i][j] == 'c':
                    visited[i][j] = turn

    # 구름을 한칸씩 오른쪽으로 옮긴다
    filed = matrixMult(filed)
    for i in range(w-1, 0, -1):
        filed[i] = filed[i-1]
    filed[0] = dot_filed
    filed = matrixMult(filed)


# 결과 표출
for i in range(0, h):
    print(' '.join(str(x) for x in visited[i]))
