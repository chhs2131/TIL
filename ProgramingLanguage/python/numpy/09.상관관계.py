import numpy as np

# var
x = np.arange(1, 100)
y = np.arange(1, 9999)
y = y[x ** 2 - 1]

# 상관관계 분석
result = np.corrcoef(x, y)
print(result)  # 1에 가까우므로 상관관계가 있음
