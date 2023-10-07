package com.lannstark.lec08

fun main() {

}

fun max(a: Int, b: Int): Int {
    return if (a > b) {
        a
    } else {
        b
    }
}

fun max2(a: Int, b: Int): Int =
    if (a > b) {
        a
    } else {
        b
    }

fun max3(a: Int, b: Int) = if (a > b) a else b

// default parameters
fun repeat(str: String, num: Int = 3, useNewLine: Boolean = true) {
    for (i in 1..num) {
        if (useNewLine) {
            println(str)
        } else {
            print(str)
        }
    }
}

// named argument
// kotlin에서 자바 함수를 가져다 쓸 때에는 사용할 수 없음
fun named(name: String, country: String) {
    println("$name is from $country")

    // named(country = "한국", name = "홍길동")  // 사용예
}

// 가변인자 (array를 인자로 줄때는 *spread 연산자를 붙여야됨)
fun printAll(vararg strings: String) {
    for (s in strings) {
        println(s)
    }
}
