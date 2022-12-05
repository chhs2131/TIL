import numpy as np

# 2차원 배열 인덱싱
array2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 인덱싱
print("인덱싱")
print(array2[0][2])  # 첫번째 행에 마지막 값을 참조하고 싶을 때 => 3
print(array2[0, 2])  # 다른 표현방법

array2[0, 2] = 100
print(array2[0, 2])  # 값 변경하기

# 2차원 배열 슬라이싱
print("\n슬라이싱")
print(array2[0:2, 1:3])  # 첫째 두번째 행에, 두번째 세번째 값을 가져온다
print(array2[:, ::2])  # 한행건너 하나만 보여줌

# 2차원 배열의 논리적 인덱싱
print("\n논리적 인덱싱")
top_tier = array2 > 5
print(array2[top_tier])  # 조건에 맞는것만 1차원 배열로 출력되게 된다.
