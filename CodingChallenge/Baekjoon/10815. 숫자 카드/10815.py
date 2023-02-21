POS_NUMBER = 10000000

# 상근이가 소유한 숫자카드는 True
input()
sang_card = [False] * 20000001
for i in list(map(int, input().split())):
    sang_card[i + POS_NUMBER] = True

# 소유한 카드면 1을 아니면 0을 결과로 저장
result = []
input()
for i in list(map(int, input().split())):
    if sang_card[i + POS_NUMBER]:
        result.append(1)
    else:
        result.append(0)

# 출력
print(*result)
