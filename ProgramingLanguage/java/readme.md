# 자바 코테대비 치트시트

고정 import
`import java.util.*;`




<br/>



## 기본 문법
```java
for (int i=0; i<100; i++)
for (var : iter)

switch(key) {
  case 1:
    break;
  default:
    return;
}
```


<br/>


## 자료구조
### Stack
```java
Stack<Integer> s = new Stack<>();
s.push(100);  // 추가 (add와 동일)
s.pop();  // 삭제 (return 존재)
s.peek();  // 조회 (삭제 X)
s.search(n);  // 특정 원소 위치 반환 (찾을 수 없으면 -1, 원소 위치는 TOP부터 1임)
s.isEmpty();  // 비어있는지 확인 (empty와 동일)
s.size();  // 총 원소 갯수
```

Tip1. 더 이상 꺼낼 원소가 없을 때, pop 또는 peek 요청을 하면 EmptyStackException 발생

Tip2. [empty() vs isEmpty()? 편한걸 써라](https://wyatti.tistory.com/entry/JAVA-Stack%EC%97%90%EC%84%9C-empty%EC%99%80-isEmpty%EB%A5%BC-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B3%A0-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0)

### Queue
```java
        Queue<Integer> q = new LinkedList<>();  // queue 자체는 interface
        q.add(100);  // 추가 (offer와 동일)
        q.add(index, n);  // 특정 위치에 추가 (e.g. [100,200]이 있을 때, add(1,300)을 하면 [100,300,200]이 됨)
        q.pop();  // 삭제 (removeFirst, remove와 동일, 값이 없는 경우 NoSuchElementException 발생)
        q.poll();  // 삭제 (pop과 동일하지만, 값이 없는 경우 null을 반환)        
        q.peek();  // 값이 없으면 null 반환
        q.isEmpty();  // empty() 없음
        q.size();
```

Tip1. pop()으로 원소를 제거해도 FIFO원칙을 따른다.

Tip2. removeFirst()와 poll()의 내부 로직 차이
```java
public E removeFirst() {
    final Node<E> f = first;
    if (f == null)
        throw new NoSuchElementException();
    return unlinkFirst(f);
}

public E poll() {
    final Node<E> f = first;
    if (f == null)
        return null;
    return unlinkFirst(f);
}
```

### List
```java
List<Integer> l = new ArrayList<>();
l.add(100);
l.add(1, 100);
l.remove(1);  // index
l.get(1);  // index
l.isEmpty();
l.size();
```

### Arrays
```java
// 배열 <-> 리스트 상호변환
l.toArray();
Arrays.asList(arr);  // int[] abc = {1,2,3,4,5}로 부터 새로운 List 생성
Stream.of(arr).toList();  // jdk 17 이후

// int[] to List<Integer>
List<Integer> l = Arrays.stream(num_list)
                        .boxed()
                        .collect(Collectors.toList());

// List<Integer> to int[]
int[] n =  l.stream()
            .mapToInt(i -> i)
            .toArray();
```

Tip1. [Array<->List 변환](https://hianna.tistory.com/551)
Tip2. [int배열을 list로 변환시 주의](https://hianna.tistory.com/552)

### Map
```java
Map<String, Integer> m = new HashMap<>();
m.put("foo", 1);
m.remove("foo");
m.clear();
```



<br/>


## 문자열
### Input
```java
Scanner sc = new Scanner(System.in);
var a = sc.nextLine();  // "안녕하세요 엔터치기 전까지 기록됩니다."
var b = sc.next();  // "띄어쓰기로구분됨"
var c = sc.nextInt();  // "1000"
var d = sc.nextDouble();  // "0.645823"
```

### String 다루기
```java
String s = "HelloWorld!";
s.length();  // 길이 출력 (11)
s.substring(3);  // 문자열 복사
s.compareTo("HelloWorld!");  // NPE 발생 가능함. 일치하지 않을시 문자사이의 거리를 알려줌
s.equals("HelloWorld!");  // null과 비교가능함 (flase 발생)
s.indexOf("Wor");  // 특정 문자가 시작하는 위치 반환 (5)
s.chartAt(1);  // 특정 인덱스에 문자 반환 (e)
s.toUpperCase();  // 문자를 모두 대문자로
s.toLowerCase();  // 문자를 모두 소문자로
s.replace(old, new);  // 해당하는 모든 문자열 치환 (e.g. replace("HiHiHi", "O") 결과는 "OOO")
s.trim();  // 양끝의 공백문자 제거
s.split(regex);  // 문자열을 해당 구분자로 잘라 배열로 반환
```
```java
String aaa = "tomato lets go";
String[] es = aaa.split("o");
for (int i = 0; i < es.length; i++) {
    System.out.print(i + "->");
    System.out.println(es[i]);
}
// 0->t
// 1->mat
// 2-> lets g
```

Tip1. [compareTo() vs equals()](https://stackoverflow.com/questions/1551235/compareto-vs-equals)

### Character: 대소문자
```java
char c = str.charAt(3);
Character.isUpperCase(c);  // 대문자인지 확인
Character.toUpperCase(c);  // 대문자로 변환
Character.toLowerCase(c);  // 소문자로 변환
Character.isWhiteSpace(c);  // 공백문자인지 확인
```

### 정규식
```java
String pattern = "^[0-9]*$"; // 숫자만 등장하는지
String str = "123321"; 

boolean result = Pattern.matches(pattern, str);
System.out.println(result); // true
```

정규식과 매칭되는 모든 글자를 치환함
```java
public String replaceAll(String regex, String replacement) {
    return Pattern.compile(regex).matcher(this).replaceAll(replacement);
}
```

Tip1. [정규표현식 규칙](https://zhfvkq.tistory.com/5)
Tip2. [정규표현식 규칙2](https://zzang9ha.tistory.com/322)



<br/>


## 형변환
```java
Integer.toString(12345);
Integer.parseInt("12345");
(new Integer(30)).intValue();  // 원시타입으로 반환
```



<br/>


## Sort
```java
List<Integer> l = new ArrayList<>();
l.add(6);
l.add(5);
l.add(3);
l.add(4);
l.add(1);
l.add(2);
```

```java
List<Integer> integers = l.stream().sorted().toList();
System.out.println(integers);  // [1, 2, 3, 4, 5, 6]
```
```java
Collections.sort(l, (a, b) -> a - b);  // [1, 2, 3, 4, 5, 6]
l.sort((a, b) -> a - b);  // [1, 2, 3, 4, 5, 6]
l.sort((a, b) -> b - a);  // [6, 5, 4, 3, 2, 1]
```

Tip1. [정렬에 대한 추가 설명](https://www.daleseo.com/java-comparable-comparator/)





<br/>



---



<br/>


[참고자료]
https://gist.github.com/Nullgom/7502a7cee30f4f052a5e5ec0d1eaa2c1
https://anjaekwang.github.io/javaCheatingSheet/



