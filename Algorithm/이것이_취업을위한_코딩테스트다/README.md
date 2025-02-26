
## 인덱스
| 번호  |이름| 책 목차   |
|-----|---|--------|
| 1   |그리디| 3, 11  |
| 2   |구현| 4, 12  |
| 3   |DFS/BFS| 5, 13  |
| 4   |정렬| 7, 14  |
| 5   |이진 탐색| 8, 15  |
| 6   |다이나믹 프로그래밍| 9, 16  |
| 7   |최단 경로| 10, 17 |
| 8   |그래프 이론| 11, 18 |
| 9   |그리디| 12     |
| 10  |기출| 19     |


## 팁

### 출제 범위
- 그리디
- 구현
- DFS/BFS (완전 탐색)
- 문자열
- 정렬
- DP
- 그래프 이론
- 자료구조

### 복잡도
- 기준 시간 제한 1초

|표기| 명칭| 가능한 N의 범위 |
|---|---|-----------|
|1| 상수 시간 |
|logN| 로그 시간 |
|N| 선형 시간 |10,000,000|
|NlogN|로그 선형 시간| 100,000   |
|N^2|이차 시간| 2,000     |
|N^3|삼차 시간| 500       |
|2^n|지수 시간|

### 파이썬 자료형
- 정수형
  - Big Integer 연산을 기본적으로 지원함
  - 단, 유효숫자에 따라서 원하는 연산결과가 나오지 않을 수 있음
- 리스트
  - 코딩테스트에서는 메모리 용량을 512MB 이내로 제한하는 경우가 많다.
  - 리스트 길이 별 메모리 사용량 추이
    - 1,000 = 4KB
    - 1,000,000 = 4MB
    - 10,000,000 = 40MB

### 스택 큐 예시
```python
# stack
stack = []
stack.append(5)
stack.append(1)
stack.pop()
print(stack)

# queue
from collections import deque  # insert, delete속도가 list에 비해 효율적
queue = deque()

queue.append(5)
queue.append(2)
queue.append(1)
queue.popleft()
queue.reverse()
print(queue)
```

### 재귀함수 예시
```python
# 재귀함수 구성 예
def factorial_recursive(n):
    # 종료조건
    if n<= 1:
        return 1
    # 재귀
    return n * factorial_recursive(n - 1)
```

### input() 대신 빠르게 입력받기
```
import sys

input_data = sys.stdin.readline().rstrip()
print(input_data)
```
