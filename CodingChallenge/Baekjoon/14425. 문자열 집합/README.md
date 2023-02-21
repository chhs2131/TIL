# 문자열 집합
- https://www.acmicpc.net/problem/14425


## 문제
- 총 N개의 문자열로 이루어진 집합 S가 주어진다.

- 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.



### 입력
- 첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 

- 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

- 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

- 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 

- 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.



### 출력
- 첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.



## 예제
### 입력 1
```python
5 11  # M S
baekjoononlinejudge  # 집합 S
startlink
codeplus
sundaycoding
codingsh
baekjoon  # 주어진 문자열 M
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
```
### 출력 1
```
4
```

### 입력 2
```python
1 1
hello
hello
```

### 출력 2
```python
1
```

### 입력 3
```python
1 1


```

### 출력 3
```python
1
```

### 입력 4
```python
3 1
h
hel
hello
hel
```

### 출력 4
```python
1
```

### 입력 5
```python
5 13
baekjoon
startlink
codeplus
sundaycoding
codingsh
baekjoononlinejudge
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
codingsh
startlink
```

### 출력 5
```python
6
```

## 참고
- 만약 문자열 m에는 중복이 없고, 집합 s에 중복이 있다면 아래와 같이 코드를 구성하면 된다.
```python
# 아래는 집합 S를 기준으로 카운트하는 코드
# 집합 S에 포함된 문자열 M을 찾기
for sss in string:
    if dic.get(sss) is False:
        dic[sss] = True

# 개수 출력 (중복 X)
count = 0
for key in dic.keys():
    if dic[key] is True:
        count += 1
print(count)
```
