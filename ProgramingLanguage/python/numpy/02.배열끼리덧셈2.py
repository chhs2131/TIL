import numpy as np

a = np.array(range(1, 11))  # 1부터 10까지 배열 생성
b = np.array(range(10, 101, 10))  # 10부터 100까지 10단위로 배열 생성

print(a + b, a - b, a * b, a / b)
