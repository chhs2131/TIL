a = input()
n = list(map(int, input().split()))

_list = [n[0]]  # n이 1개일경우에 예외처리필요
min_n = n[0]
pasta = [0]
pasta_max = 0
i = 1
while i < len(n):
    now = n[i]
    result = now - min_n
    if result > pasta_max:
        # 조건에 맞는 경우 현재 결과를 사용한다.
        pasta.append(result)
        pasta_max = result
        pass
    else:
        # 조건에 맞지 않는 경우 이전 결과를 사용한다.
        pasta.append(pasta_max)
        pass
    if n[i] < min_n:  # min 값을 갱신한다.
        min_n = n[i]
    i += 1

result = str(pasta).replace('[', '').replace(']', '').replace(',', '')
print(result)
