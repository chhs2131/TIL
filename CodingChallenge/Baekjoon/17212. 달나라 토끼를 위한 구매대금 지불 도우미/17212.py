# 입력 받기 (지불할 금액)
n = int(input())

# 변수 초기화
coin_list = [2, 5, 7]
count = [_ for _ in range(n + 1)]

# 각 동전별로 최소 금액 확인 (작은거에서 큰걸로)
for coin in coin_list:
    for price in range(coin, n + 1):
        count[price] = min(count[price], count[price - coin] + 1)

# 결과 출력
print(count.pop())
