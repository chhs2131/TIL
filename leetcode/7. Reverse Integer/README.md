# 7. Reverse Integer

int형(32비트) 정수가 입력으로 주어졌을 때, 이 입력을 반대로 뒤집어서 반환하면 됩니다.

뒤집은 숫자가 int형을 초과할 때는 숫자 0을 반환합니다.

또한 해당 시스템에서는 64비트 int형(long long)은 사용할 수 없는 것으로 가정합니다.

> https://leetcode.com/problems/reverse-integer/ 
>
> Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
>
> Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
<br/>


## 입출력 예제

```
Example 1:
Input: x = 123
Output: 321
```

```
Example 2:
Input: x = -123
Output: -321
```

```
Example 3:
Input: x = 120
Output: 21
```

```
Example 4:
Input: x = 0
Output: 0
```

범위: -2^31^ <= x <= 2^31^ - 1  
<br/>
  

## 코딩 전 생각해볼만한 사항

* 숫자를 뒤집는 방법은, 숫자를 하나 뽑은 뒤  원하는 자리로 가도록 10, 100, 1000, ... 을 곱해주면 됩니다.
* 32비트 int형의 범위는 **-2,147,483,648 ~ 2,147,483,647** 입니다. 

- 양수와 음수를 구분지어 처리하기 힘들다면, 모든 입력을 **양수(절대값)로 만들어서 처리**하면 됩니다.

- 1000000009을 뒤집으면 90억이되어 예외조건(32비트 int형 보다 크기가 큼)에 해당됩니다.
<br/>
  

## 플로우차트 (FlowChart)

->input image
<br/>


## 핵심코드

1. 숫자뒤집기  
   아래 코드를 베이스로 숫자 뒤집기를 구현 할 수 있습니다.

   ```cpp
   int x = 1234;
   int result = 0;
   
   for(int i=0; x != 0; i++) {
     result += (x % 10) * pow(10,3-i); //숫자 하나를 뽑아서, 10에 n승을 곱합니다.
     x = x / 10;
   }
   std::cout << result; //출력 : 4321
   ```

   원래 숫자의 단위가 몇인지는 log10 함수를 통해 확인 할 수 있습니다.

   >  int digits = (int) log10(x);

   
<br/>
2. 음수/양수 구분없이 처리하기
    몇의 자리 숫자인지 알아내기 위해 log10 함수를 사용하는 경우, 양수의 경우 값을 구하는데 문제가 없습니다. 하지만 음수의 경우 문제가 생깁니다. 이를 해결하기위해 입력된 수를 확인하여 음수인 경우 우선 양수로 변환하여 처리한 뒤에 다시 음수로 만들어주는 스킬이 필요합니다.

   ```cpp
   //마이너스인지 확인해서 마이너스면 양수로 전환
   bool minus = false;
   if (x < 0) {
   	minus = true;
   	x *= -1;
   }
   
   //마이너스 숫자였던 경우 마이너스 붙여주기
   if (minus)
   	x *= -1;
   ```

   
<br/>
3. 가장 작은 음수에 대한 예외처리
    위와 같이 음수를 양수로 바꾸는 경우 한가지 문제점이 있습니다. int형 변수의 범위는 다음과 같습니다. 

   >(32비트) int의 범위 : -2^31^ <= x <= 2^31^ - 1

    양수와 음수 모두 2^31^ 이라는 절대값을 보이는데, 자세히보시면 양수의 경우 절대값에서 **1** 만큼을 뺀것을 볼 수 있습니다. 즉, 가장작은 음수가 가장큰 양수보다 1만큼 더 큰 것입니다. 만약 가장작은 음수에 -1을 곱하여 양수로 만든다면 int형의 범위를 벗어나게 됩니다.
    따라서 해당 수에 대해서는 미리 예외처리를 해줘야합니다. 코드는 아래와 같습니다.

   ```cpp
   //INT_MIN(-2,147,483,648)인 경우 0을 반환.
   if (x == INT_MIN)
   	return 0;
   ```

   
<br/>
4. int형 범위안에 있는지 확인하기
   아래 코드는 숫자뒤집기를 작은 자릿수부터 순차적으로 실행하면서, 해당 수가 int형 범위안에 있는지 확인하는 코드입니다. 개념적인 특징은 다음과 같습니다.

   * 최초입력된 숫자가 10억보다 작은 경우 검사를 진행할 필요가 없다.
   * 뒤집힌 숫자가 INT_MAX의 해당 자릿수보다 작다면(미만) 검사를 더이상 진행할 필요가 없다.

   ```cpp
   //숫자 뒤집기 실행.
   int result = 0;
   bool max_check = true;
   int intmax[10] = { 2,1,4,7,4,8,3,6,4,7 };
   for (int i = 0; i <= digits; i++) {
       int new_num = x % 10;
   
       //x가 10억 단위인 경우, 진행시 문제가 되는지 확인 (int => 32bit)
       if (digits >= 9) {
       if (max_check) {
       if (new_num > intmax[i]) //현재숫자가 int형보다 크다면 0을 반환한다.
       return 0;
       else if (new_num == intmax[i]) //현재숫자가 int형과 같다면 다음 숫자를 계속 검사한다.
       max_check = true;
       else //현재숫자가 int형보다 작다면 이후 숫자들은 검사할 필요가 없다.
       max_check = false;
       }
   }
   
   result += new_num * (int)pow(10, digits - i);
   x /= 10;
   ```

   
<br/>
## 실행 예시

=> 이미지




<br/>
=> 이미지
