# 이진탐색
- 탐색 범위가 2,000만건을 넘어간다면 이진 탐색으로 접근
- 1,000만건을 넘을 때 이진 탐색 고려 (logN)
- 계수 정렬로 해결이 가능한 상황일 수도 있다.
- sort()는 N * logN 의 시간복잡도를 가짐


- 시작점, 끝점, 탐색범위내의 중간값 세개를 기준으로 탐색을 진행함
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_serach(array, target, 0, n - 1)
if result == None:
    print("nope")
else:
    print(result + 1)
```