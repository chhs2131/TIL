n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))  # 한줄씩 입력받으면서
    min_value = min(data)  # 각 행에 있는 가장 작은 숫자를 뽑는다.
    result = max(result, min_value)  # 매행에서 뽑은 숫자 중 가장 큰 수를 기억한다.

print(result)
