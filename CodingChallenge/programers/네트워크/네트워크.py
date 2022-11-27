def solution(n, computers):
    answer = 0

    v = [False for i in range(n)]
    next_target = []
    for i in range(n):
        # 네트워크의 시작점을 만나면 카운트한다.
        if v[i] == False:
            next_target = [i]
            answer += 1

        for nt in next_target:
            # 방문 처리
            v[nt] = True

            # 연결되어있는 것 중 아직가보지 않은 경우, 다음에 방문할 곳으로 추가
            for j in range(n):
                if computers[nt][j] == 1:
                    if v[j] == False:
                        next_target.append(j)

    return answer
