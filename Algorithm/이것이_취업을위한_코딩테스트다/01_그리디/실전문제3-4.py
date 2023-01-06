n, k = map(int, input().split())
result = 0

while True:
    # K로 나누어 떨어질 때 까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    n = target

    # N을 K로 나눌 수 없다면 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //= k

# 남은 수만큼 1씩 빼기 진행
result += (n - 1)
print(result)
