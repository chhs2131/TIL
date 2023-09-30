package com.lannstark.lec04

fun main() {
    val money1 = JavaMoney(2000L)
    val money2 = JavaMoney(1000L)
    val money3 = JavaMoney(1000L)
    val money4 = money3

    // compare to
    if (money1 > money2) {
        println("money1이 더 큽니다")
    }

    // 동등성 동일성
    if (money2 == money3) {
        println("money2과 money3가 같습니다")
    }
    if (money3 === money4) {
        println("money3,4는 같은 레퍼런스입니다.")
    }
}