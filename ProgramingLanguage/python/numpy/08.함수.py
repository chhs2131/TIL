import numpy as np

# range와 동일하게 동작하는 함수 -> 단, 결과로 np 리스트를 생성한다.
print(np.arange(1, 6))  # 1, 2, 3, 4, 5
print(np.arange(1, 10, 2))  # 1, 3, 5, 7, 9

# linspace - 균일한 간격으로 n개의 숫자를 생성한다.
print(np.linspace(0, 10, 9))  # 0부터 10까지 총 9개의 숫자들을 생성한다. 단, 일정한 간격을 유지한다.

# logspace - 로그 스케일로 수를 생성한다.
print(np.logspace(0, 10, 9))


# reshape - 데이터 개수를 유지한채 배열의 차원을 변경한다.
x = np.arange(12)
print(x)
x = x.reshape(3, 4)  # 3행, 4열로 제작한다.
print(x)

# flatten - 일차원 배열로 만들어버린다.
x = x.flatten()
print(x)

# random - 난수 생성
print(np.random.randn(5))  # <- 5개의 난수 (0~1)
print(np.random.randn(3, 4))  # 3행 4개의 난수 => 총 12개
