package com.lannstark.lec17

fun main() {
    val fruits = listOf(
        Fruit("사과", 1_000),
        Fruit("사과", 1_200),
        Fruit("사과", 1_300),
        Fruit("사과", 1_400),
        Fruit("사과", 1_500),
        Fruit("바나나", 2_000),
        Fruit("바나나", 2_700),
        Fruit("바나나", 3_300),
        Fruit("수박", 10_000),
    )

   // 람다 작성 방식
    val isApple = fun(fruit: Fruit): Boolean {
        return fruit.name == "사과"
    }

    val isApple2 = { fruit: Fruit -> fruit.name == "사과"}

    // 람다 사용 예시
    isApple(fruits[0])
    isApple.invoke(fruits[0])

    // 익명 함수 인자로 전달
    filterFruits(fruits, isApple)
    filterFruits(fruits) { fruit: Fruit -> fruit.name == "사과" }
    filterFruits(fruits) { fruit -> fruit.name == "사과" }
    filterFruits(fruits) { it.name == "사과" }
}

private fun filterFruits(
    fruits: List<Fruit>, filter: (Fruit) -> Boolean
): List<Fruit> {
    // 아래 부분도 stream처럼 선언식으로 사용할 수 있음
    val results = mutableListOf<Fruit>()
    for (fruit in fruits) {
        if (filter(fruit)) {
            results.add(fruit)
        }
    }
    return results
}
