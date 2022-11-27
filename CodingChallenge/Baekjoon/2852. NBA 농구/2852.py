# a번팀 MM:SS에 득점
import datetime

if __name__ == "__main__":
    # 입력
    n = int(input())
    scoreboard = []
    for i in range(0, n):
        scoreboard.append(list(input().split()))

    # 연산진행
    before = datetime.datetime.strptime("00:00", '%M:%S')
    score = 0
    b_score = score
    team1 = before
    team2 = before
    for i in range(0, n):
        # 득점상황 발생!
        target = datetime.datetime.strptime(scoreboard[i][1], '%M:%S')
        if scoreboard[i][0] == '1':
            score = score - 1
        else:
            score = score + 1

        # 이기고 있는 팀에게 시간 배분
        if i != 0:
            if b_score == 0:
                pass
            elif b_score < 0:
                team1 = team1 + (target - before)
            elif b_score > 0:
                team2 = team2 + (target - before)

        # 현재 시각을 이전값으로 등록
        before = target
        b_score = score

    # 라스트 골 처리
    endtime = datetime.datetime.strptime("48:00", '%M:%S')
    if score == 0:
        pass
    elif score < 0:
        team1 = team1 + (endtime - before)
    elif score > 0:
        team2 = team2 + (endtime - before)

    # 결과 출력
    print(team1.strftime('%M:%S'))
    print(team2.strftime('%M:%S'))
