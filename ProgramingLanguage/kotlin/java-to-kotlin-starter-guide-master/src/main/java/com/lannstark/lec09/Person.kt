package com.lannstark.lec09

fun main() {
    val person = JavaPerson("홍길동", 10)
    println(person.name)
    println(person.age)
}

class Person(val name: String, var age: Int) {  // 생성자 지시어 constructor 는 생략가능
//    val name = name  // getter setter를 자동으로 생성함
//    var age = age

    init {  // 클래스가 초기화되는 시점에 실행되는 블록
        if (age <= 0) {
            throw IllegalArgumentException("age must be positive")
        }
    }

    constructor(name: String): this(name, 1) {
        println("name: " + name)  // 부생성자안에 다른 블럭이 있어도 된다..만 디폴트 생성자와 정적 팩토리 메소드를 추천
    }

//    fun isAdult(): Boolean {
//        return this.age >= 20
//    }

    val isAdult: Boolean
        get() = this.age >= 20
}