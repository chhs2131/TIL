# Dart 기초 문법
- dart는 객체지향 언어이다.
- 객체지향 코딩을 해본 사람을 위한 가볍게 훑어보기용 문서가 목표
- cascade operator 때문에 반드시 구문의 끝에 ; 을 달아줘야한다.
- 생성자가 없는 클래스를 with 으로 호출하여 내부코드를 재사용 할 수 있다. (mixin)
표
## HelloWorld
```dart
void main() {
    print("hello world!");
}
```

## 변수
- 자료형 종류: var, Object, String, Numbers(int, double), bool, Records, Collections(List, Set, Map), Runes, Symbol, generics`<T>`, null ...
- 기본적으로 DefaultValue는 null 이지만, 초기화되지 않은 변수를 호출 할 수 없다. (nullSafety)


### dynamic type var
```dart 
var autoType = "변수 생성과 동시에 값을 할당하면 컴파일타임에서 타입이 지정되어 타입변경불가";  //autoType = 1 불가능

var name;
name = 123;
name = "이것은 Dynamic Var로 런타임에서 타입변경이 가능";

dynamic but;
if(but is String) {
  but = "dynamic으로 타입을 선언하는 것이 기능,가독성면에서 유리함";
}
```

### nullable var
- 특정 버전이상의 Dart 언어는 기본적으로 nullSafety함
- Type? 처럼 타입뒤에 `?` 를 붙여 nullable을 명시해줄 수 있음
- 또한 변수명? 처럼 변수명 뒤에 `?`를 붙여 null이 아닌경우에만 동작을 이어나가도록 할 수 있음
```dart
String? nullString = null;
nullString?.isEmpty; // nullString이 null이 아니면 isEmtpy method를 호출 
```

### 수정자

```dart
// final (변경불가능한 값. js의 const)
final pie = 3.1415;

// late (초기 데이터 없이 변수 선언가능, 값대입전에 해당 변수를 호출하면 경고가 발생함) ??????? var도 되지않나
late int b;  // late뒤에는 Type을 입력해줘야한다.
b = 2;

// const (상수. final처럼 수정 불가 + 컴파일타임.앱스토어에 올라가기전에 알고있는 값. java static final?) 
const String API_KEY = "123456";
```

### qq 연산자
- 값이 null인 경우에만 지정된 행동을 하도록 명시

```dart
String? qq;
qq ??= "qqq";
qq ??= "abc";  //컴파일러? IDE에서 에러 발생 (can't be null)
print(qq);  // qqq 가 출력됨
```

### String Interpolation 
- 문자열 중간에 달러사인($)과 함께 변수명을 언급하면, 문자열에 바로 대입할 수 있음
- 문자열끼리는 + 로도 연산이 가능함 (e.g. "대한민국" + "화이팅!")
- 달러사인과 대괄호를 조합하여 
```dart  
String address = "대한민국";
int count = 0;
String greeting = "$address에 ${count + 1}번째 방문을 환영합니다!";
print(greeting);  // 대한민국에 1번째 방문을 환영합니다!
```
 


## Collections
- List, Set, Map이 존재한다.
- array가 아니기 때문에 `List[1] = 1;` 과 같은 구문은 사용할 수 없다.
- `var items = {}` 라고 선언하면 map이 생성된다. (not set)
- `var list = [1, 2, 3, ...anotherList]` 라고 명시하면 초기화단계에서 다른 리스트에 원소를 모두 추가 할 수 있다.


```dart
// Lists
List<int> nums = [1,2,3,4,5,6, if(true) 7, if(false) 8,];  // if를 통해 판단하는 것을 controlFlow operators라고 함
nums.add(9);
nums.first;
nums.contains(4);

List<int> favoriteNums = [
  0,
  10,
  100,
  for (int number in nums) number + 1000,
];
print(favoriteNums);  // [0, 10, 100, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1009]
print(nums);  // [1, 2, 3, 4, 5, 6, 7, 9]


// maps (dict.)
Map<String, Object> store = {
  "apple": 1000,
  "banana": 2000,
  "opend": false
};
store.entries;
store.containsKey;
store.putIfAbsent;


// sets (중복 원소 x)
Set<int> lotto = {1, 2, 3, 4, 1, 1};
lotto.add(3);
print(lotto);  // {1, 2, 3, 4}
``` 
  

## Function
- 자바의 Method와 유사, 하지만 C, Python처럼 Function만 단독으로 존재할 수 있음
- 인터페이스에서 선언하는건 아니지만, 자바 @FunctionalInterface 처럼 함수형으로 사용 가능
- 인자를 전달할 때 순서기반으로 할지 인자명을 기반으로 할지 지정가능 (python 함수 처럼 `func(name="a", age=3)` 같은 방식 가능)
    - 반드시 입력해야하는 인자에는 required를 선언
    - 그렇지 않은 경우 defaultValue를 선언
- Optional Positonal Params를 지원해서 defaultValue가 있는 인자만 `[int? money = 0]`와 같은 형태로 선언해주면 된다.
- 가변인자를 지원하지 않지만, 위 기능들을 조합해 흉내 낼 수 있다.

```dart
// Function(method)
void sayHello(String name) {
  print("Hello $name!");
}

// Function (함수형, @FunctionalInterface)
String helloSentence(String name) => "Hello $name";

// NameArgument (map 느낌으로 함수에 인자를 전달하는 방법, 이 경우 기본값을 지정하거나 required 선언이 필요)
void setPlayer({required String name, String country = '-', int age = 0}) {
  print(name + "/" + country + "/" + age.toString());
}

// Function - Optional Positonal Params
void optionalHello(String name, [String? country = '-']) {
  print(name + " / $country");
}
```

- 함수 실과 결과
```dart
// Function
setPlayer(
  name: "먼그옛날",
  age: 11,
);  // 먼그옛날/-/11

optionalHello("먼그옛날");
optionalHello("먼그옛날", "인천");
```

## Class
- class, abstract, 상속(extends, implements) 등의 개념이 존재한다. 
- with(mixin)을 사용하여 생성자가 없는 class 조각을 포함시킬 수 있다.

### Class
- member변수는 var, dynamic이 아닌 명확한 type을 명시해줘야한다.
- 기본 생성자 + 이름을 지정하면 정적팩토리 메소드를 만들 수 있다출

```dart
class Player {  // 멤버변수는 반드시 type 명시
  final String name;
  int age, money;
  
  // Player(this.name, this.age);
  Player({
    required this.name,
    required this.age,
    this.money = 0,
  });
  
  // namedConstructor (정적팩토리 메소드 패턴)
  Player.nameConstructor({required String name, required int age}):
    this.name = name,
    this.age = age,
    this.money = 0;
  
  String getName() {
    return name;
  }
}
```

- 인스턴스 생성 및 호출
```dart
// Class
// Player player = Player("먼그옛날", 11);
// print(player.getName());

Player player = Player(age: 70, name: "john");
print(player.getName());

Player player2 = Player.nameConstructor(name: "먼그옜날", age:99);
print(player2.getName());
```

### abstract
- class 앞에 abstract를 명시하여 추상객체를 생성할 수 있다.
- 상속받은 클래스는 `super`를 통해 부모의 기능을 호출 할 수 있다.

```dart
abstract class Fruit {
  void taste() {
    print("good~");
  }
}

class Banana extends Fruit {
}

class Apple extends Fruit {
  @override
  void taste() {
    super.taste();
    print("bad!");
  }
}
```

- 실행결과
```dart
Fruit apple = Apple();
Fruit banana = Banana();
apple.taste();  // good, bad
banana.taste();  // good
```

### mixin
- mixin으로 명시하거나, 생성자가 없는 class 모두 mixin이 된다.
- class 정의시에 with 구문 뒤에 mixin을 명시하여 관련 코드를 사용 할 수 있다.

```dart
mixin itmeA {
  void hello() {
    print("hello");
  }
}

class itemB {
  void bye() {
    print("bye bye");
  }
}
```

- 실행결과
```dart
class welcomeBot with itemA, itemB {
}

void main() {
  var bot = welcomeBot();
  bot.hello();  // hello
  bot.bye();  // bye bye
}
```

### cascade operator
- `..` 을 통해 특정 Object에 대해 연속적으로 함수호출, 필드 접근 등을 순서대로 수행할 수 있음
- `stream` 개념과 다른 점은 각 단계에서 수행된 결과에 대해 접근하지 않음
- 아래 cascade operator를 사용했을 때와 하지않았을 때를 비교하면 좋으며, 단순 편의용 기능!
- 아래와 같은 `Person` 클래스가 있을 때,
```dart
class Person {
  String name;
  int age;
  
  Person(this.name, this.age);
  
  void introduce() {
    print("Hello, my name is $name and I am $age years old.");
  }
}
```

- 기존 방식
```dart
void main() {
  var person = Person("John", 30);
  person.introduce();
  person.age = 31;
  person.introduce();
}
```

- 사용하였을 때
```dart
void main() {
var person = Person("John", 30)
  ..introduce()
  ..age = 31
  ..introduce();
}
```
