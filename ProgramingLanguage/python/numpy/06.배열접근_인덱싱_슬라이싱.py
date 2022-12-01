import numpy as np

scores = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# 인덱스 접근
print("인덱스 접근")
print(scores[2])  # 2
print(scores[-1])  # 8

# 슬라이싱
print("\n슬라이싱")
print(scores[1:4])  # 1, 2, 3
print(scores[3:])  # 3, 4, 5, 6, 7, 8
print(scores[4:-1])  # 4, 5, 6, 7

# 논리적 인덱싱
print("\n논리적 인덱싱")
top_tier = scores > 5
print(top_tier)  # false, false, false, false, false, false, true, true, true
print(scores[top_tier])  # 조건에 해당(ture)하는 6, 7, 8

# 예제 - 'c'만 추출하기
print("\n예제")
x = np.array([['a', 'b', 'c', 'd'], ['c', 'c', 'g', 'h']])
print(x[x == 'c'])

# 예제2 - mat_a - mat_b = ?
print("\n예제2")
mat_a = np.array([[10, 20, 30], [10, 20, 30]])
mat_b = np.array([[2, 2, 2], [1, 2, 3]])
print(mat_a - mat_b)
