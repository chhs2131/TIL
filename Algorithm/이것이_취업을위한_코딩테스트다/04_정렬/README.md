# 정렬

- 연산에 필요한 횟수 데이터가 1000개일 때, 선택삽입(1,000,000) vs 퀵(10,000)

| 정렬       | n=100      | n=1000    | n=10000  |
|----------|------------|-----------|----------|
| 선택,삽입    | 0.0123     | 0.354     | 15.475   |
| 퀵        | 0.00156    | 0.00343   | 0.0312   |
| sorted() | 0.00000753 | 0.0000365 | 0.000248 |
| 삽입       | N^2        |

<br/>

- 계수정렬
    - 특정 조건이 부합할 때만 사용 가능
    - 일반적으로 가장 큰 데이터와 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능
    - O(N+K)
- sorted() or sort()
    - 파이썬의 내장 정렬 라이브러리
    - 병합 정렬을 기반으로 만들어짐
    - O(NlogN)을 보장함

```python
# sort
array = [7, 5, 9, 0, 3, 1, 6,, 2, 4, 8]
array.sort()

# sort with key
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
```

<br/>

## 예제
### 실전문제 6-2 (위에서 아래로)
```python
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
```

<br/>

### 실전문제 6-3 (성적이 낮은 순서로 학생 출력하기)
```python
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))

array = sorted(array, key=lambda student: student[1])
for student in array:
    print(student[0], end=' ')
```

<br/>

### 실전문제 6-4 (두 배열의 원소 교체)
```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))
```
