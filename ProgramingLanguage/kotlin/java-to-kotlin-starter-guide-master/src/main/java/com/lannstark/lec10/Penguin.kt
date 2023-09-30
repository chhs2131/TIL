package com.lannstark.lec10

class Penguin (
    species: String
) : Animal(species, 2), Swimable, Flyable {
    private val wingCount: Int = 2

    override fun act() {
        super<Swimable>.act()
        super<Flyable>.act()
    }

    override fun move() {
        println("펭귄 발걸음 촵촵")
    }

    override val legCount: Int  // property를 override하려면 반드시 open 키워드를 붙여줘야함
        get() = super.legCount + this.wingCount

    override val swimAblity
        get() = 3
}