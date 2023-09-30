package com.lannstark.lec06

fun main() {
    // for
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7)
    for (number in numbers) {
        println(number)
    }

    // i for
    for (i in 1..3) {
        println(i)
    }

    for (i in 3 downTo 1) {
        println(i)
    }

    for (i in 1..5 step 2) {
        println(i)
    }

    // progression(등차수열) and range
}
