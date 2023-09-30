package com.lannstark.lec05

fun validateScoreIsNotNegative(score: Int) {
    if (score < 0) {
        throw IllegalArgumentException("${score} Score cannot be negative")
    }
}

// Statement 내에 Expression이 위치한다.
// Expression: 하나의 값으로 반환된다.
// 자바에서는 if-else가 Statement이지만, 코틀린에서는 아니기 때문에 바로 반환(값)할 수 있다.
fun getPassOrFail(score: Int): String {
    return if (score >= 60) {
        "Pass"
    } else {
        "Fail"
    }
}

// if
fun getGrade(score: Int): String {
    return if (score >= 90) {
        "A"
    } else if (score >= 80) {
        "B"
    } else if (score >= 70) {
        "C"
    } else {
        "D"
    }
}

// if
fun isScoreInRange(score: Int): Boolean {
    if (score !in 0..100) {  // beteween
        return false
    }
    return true
}

// switch
fun getGradeWithSwitch(score: Int): String {
    return when {
        score in 90..100 -> "A"
        score in 80..89 -> "B"
        score in 70..79 -> "C"
        else -> "D"
    }
//    return when {
//        score >= 90 -> "A"
//        score >= 80 -> "B"
//        score >= 70 -> "C"
//        else -> "D"
//    }
}

// when
fun isStringType(obj: Any): Boolean {
    return when (obj) {
        is String -> true
        else -> false
    }
}

// when
fun juddgeNumber2(number: Int) {
    when {  // early return 처럼 사용할 수 있음,
        number == 0 -> println("주어진 숫자는 0입니다.")
        number %2 == 0 -> println("주어진 숫자는 짝수입니다.")
        else -> println("주어진 숫자는 홀수입니다.")
    }
}
