package com.lannstark.lec12

fun main() {
    moveSometing(object : Movable{
        override fun move() {
            println("무브무브")
        }
        override fun fly() {
            println("날다날다")
        }
    })
}

private fun moveSometing(movable: Movable) {
    movable.move()
    movable.fly()
}
