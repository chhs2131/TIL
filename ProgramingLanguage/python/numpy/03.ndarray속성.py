import numpy as np


def print_attribute(a):
    print("\n===[정보]===")  # [1,2,3] 기준
    print("차원별 원소 크기", a.shape)  # (3,)
    print("차원의 갯수", a.ndim)  # 1
    print("객체 내부 자료형", a.dtype)  # int32
    print("객체 내주 자료형이 차지하는 메모리 크기", a.itemsize)  # 4
    print("항목의 수", a.size)  # 3


arr1 = np.array([1, 2, 3])
print_attribute(arr1)

arr2 = np.array(range(1, 11)) + np.array(range(10, 101, 10))
print_attribute(arr2)
