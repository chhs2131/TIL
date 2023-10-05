package com.lannstark.lec14

// 상속받을 수 있는 Enum class
// 단, 같은 패키지 내에서만 상속이 가능함
sealed class HyundaiCar(
    val name: String,
    val price: Long
)

class Avante : HyundaiCar("아반떼", 1_000L)
class Sonata : HyundaiCar("소나타", 2_000L)
class Grandeur : HyundaiCar("그랜저", 3_000L)


// enum과 마찬가지로 when expression 가능
fun handleHyundaiCar(car : HyundaiCar) {
    when (car) {
        is Avante -> println("아반떼")
        is Sonata -> println("소나타")
        is Grandeur -> println("그랜저")
        // 마찬가지로 else 분기에 대한 처리는 필요하지 않음
    }
}
