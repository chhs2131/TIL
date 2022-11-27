import sys
input = sys.stdin.readline

case_count = 0
while True:
    # 변수 초기화
    case_count += 1
    end_flag = False
    tree_flag = True
    edge = []

    # 입력
    while True:
        edge += list(map(int, input().split()))
        if edge:  # 공백입력은 미친것인가요? 🤔
            if edge[-1] == 0 and edge[-2] == 0:
                break
            elif edge[-1] == -1 and edge[-2] == -1:  # 프로그램 종료 처리
                end_flag = True
                break
    if end_flag:
        break

    # 탐색
    line = [[] for _ in range(1000)]  # 입력이 최대 13개 이다.
    have_coming_line = []
    v = {}

    # 간선 형태로 정리
    e = edge.pop()
    s = edge.pop()
    if len(edge) == 0:  # 아무것도 없는 그래프 예외처리
        print("Case", case_count, "is a tree.")
        continue

    while edge:
        e = edge.pop()
        s = edge.pop()
        v[s] = False
        v[e] = False
        have_coming_line.append(e)
        line[s].append(e)

    # 루트 노드를 찾고 (연결된게 없는 것을 기준)
    root = None
    for item in v.keys():
        if item not in have_coming_line:
            if root is None:
                root = item
            else:
                tree_flag = False
                break

    if root is None:  # 적절한 루트 노드가 없는 경우 예외처리
        print("Case", case_count, "is not a tree.")
        continue

    # 거기서 부터 탐색 시작
    n = [root]
    while n:
        # 방문처리 진행
        now = n.pop()

        # 연결된 것들을 추가
        for l in line[now]:
            if v[l]:
                tree_flag = False
                break
            else:
                v[l] = True
                n.append(l)

    # 루트노드 1개를 제외하고, 모두 방문했는지(count==1) 확인
    count = 0
    for i in v:
        if not v[i]:
            count += 1
            pass
    if count != 1:
        tree_flag = False

    # 최종 출력
    if tree_flag:
        print("Case", case_count, "is a tree.")
    else:
        print("Case", case_count, "is not a tree.")

    # print(count, n, "\n", line, "\n", v)

'''
# 간선 갯수로 세려고 한거 (실패)

import sys
input = sys.stdin.readline

case_count = 0
while True:
    # 변수 초기화
    case_count += 1
    end_flag = False
    edge = []
    visit = {}

    # 입력
    while True:
        edge += list(map(int, input().split()))
        if edge[-1] == 0 and edge[-2] == 0:
            break
        elif edge[-1] == -1 and edge[-2] == -1:  # 끝남 처리
            end_flag = True
            break
    if end_flag:
        break

    # 탐색
    while edge:
        e = edge.pop()
        s = edge.pop()
        if e in visit.keys() and visit[e]:  # 이미 방문한 적 있는 경우
            end_flag = True
            break
        visit[e] = True
        if s not in visit.keys():
            visit[s] = False

    # 출력
    if end_flag:
        print("Case", case_count, "is not a tree.")
    else:
        count = 0
        if len(visit) == 1:
            count = 1
        else:
            for v in visit:
                if not visit[v]:
                    count += 1
        if count == 1:
            print("Case", case_count, "is a tree.")
        else:
            print("Case", case_count, "is not a tree.")

'''
