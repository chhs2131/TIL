package com.lannstark.lec02

fun main() {
    // safe call
    val str: String? = "ABC"
    println(str?.length)  // 3

    val str2: String? = null
    println(str2?.length)  // null

    // elvis (??)
    val str3: String? = null
    println(str3?.length?: 0)  // 0
}

fun startsWithA1(str: String?): Boolean {
    return str?.startsWith("A")
        ?: throw IllegalArgumentException("it is null");

//    if (str == null) {
//        throw IllegalArgumentException("it is null")
//    }
//    return str.startsWith("A")
}

fun startsWithA2(str: String?): Boolean? {
    return str?.startsWith("A");

//    if (str == null) {
//        return null
//    }
//    return str.startsWith("A")
}

fun startsWithA3(str: String?): Boolean {
    return str?.startsWith("A")?: false
//    if (str == null) {
//        return false
//    }
//    return str.startsWith("A")
}

fun startsWith(str: String?): Boolean {
    return str!!.startsWith("A")  // 절대 null이 될 수 없음, 하지만 null이 들어온다면? NPE 발생
}
