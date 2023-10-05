package com.lannstark.lec15

fun main() {
    // 배열 사용하기
    val array = arrayOf(100, 200)
    array.plus(300)

    for (i in array.indices) {
        println("$i ${array[i]}")
    }
    for ((idx, value) in array.withIndex()) {
        println("$idx $value")
    }

    // List 사용하기 (빈 배열은 emptyList<Int>()로 선언가능)
    val numbers = listOf(100, 200)  // 가변은 mutableListOf
    println("${numbers.get(0)} or ${numbers[0]}")

    // Map 사용하기
    val oldMap = mutableMapOf<Int, String>()
    oldMap[1] = "one"
    oldMap[2] = "two"

    mapOf(3 to "three", 4 to "four")  // 불변맵 초기 선언. 중위 호출을 통해 대입

    for (key in oldMap.keys) {
        println("$key is $oldMap[$key]")  // or oldMap.get(key)
    }
    for ((key, value) in oldMap.entries) {
        println("$key is $value")
    }
}
