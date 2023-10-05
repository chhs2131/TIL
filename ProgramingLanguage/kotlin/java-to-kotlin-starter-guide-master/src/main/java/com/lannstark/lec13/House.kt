package com.lannstark.lec13

// static한 inner class
class House (
    private var address: String,
    private var livingRoom: LivingRoom
) {
    class LivingRoom(
        private var area: Double
    )
}

// 권장되지않는 부모를 참조하는 inner class
class HouseRefer (
    private var address: String,
    private var livingRoom: LivingRoom
) {
    inner class LivingRoom(
        private var area: Double
    ) {
        val address: String
            get() = this@HouseRefer.address  // 상위 클래스를 참조할 때는 this@이름 을 사용해야한다.
    }
}
