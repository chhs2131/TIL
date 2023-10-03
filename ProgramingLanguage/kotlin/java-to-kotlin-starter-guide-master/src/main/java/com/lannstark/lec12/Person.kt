package com.lannstark.lec12

fun main() {
    println(Person.singleton.a)
    Person.singleton.a += 10
    println(Person.singleton.a)
}

class Person private constructor(
    val name: String,
    val age: Int
) {
    // static 처리 (아래와 같이 companion object를 선언하거나, 파일 최상단에 선언하기)
    companion object Factory : Log {
        private const val MIN_AGE = 1
        fun newBaby(name: String): Person {
            return Person(name, MIN_AGE)
        }

        override fun log(message: String) = println(message)
    }

    // singleton 은 object 지시어를 붙여주면 끝
    object singleton {
        var a: Int = 0
    }
}
