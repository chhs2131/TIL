# 동전으로 거스름돈을 줄 때 최소개만 주기
# 동전종류: 500, 100, 50, 10
# 입력: 거슬러줘야 할 돈 N
# 제한사항: 입력은 항상 10의 배수이다.

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
