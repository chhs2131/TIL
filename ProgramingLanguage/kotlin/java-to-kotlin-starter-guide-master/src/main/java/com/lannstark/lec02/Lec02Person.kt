package com.lannstark.lec02

fun main() {
    val person = Person("개발자")
    startsWithA(person.name)  // 코틀린에서는 자바의 nullable 어노테이션을 확인할 수 있음
}

fun startsWithA(str: String?): Boolean {
    return str?.startsWith("A") ?: false
}

// 플랫폼타입 -> nullable인지 정보를 확인할 수 없는 타입
