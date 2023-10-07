package com.lannstark.lec16

fun main() {
    val str = "ABC"
    println(str.lastChar())  // C

    val person = Person("HS", "Choi", 100)
    println(person.nextYearAge())
}

// 기존 클래스에 멤버함수처럼 작동하는 확장함수
// 단, 캡슐화를 깰순 없기 때문에 private, protected 인 경우는 멤버는 가져올 수 없다.
fun String.lastChar(): Char {
    return this[this.length - 1]
}

// 멤버함수와 확장함수의 시그니처(이름)이 동일하면 멤버함수를 우선 호출한다.
fun Person.nextYearAge(): Int {
    println("확장 함수")
    return this.age + 1;
}
