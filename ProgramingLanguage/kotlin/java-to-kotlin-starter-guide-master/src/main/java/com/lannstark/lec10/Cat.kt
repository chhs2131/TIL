package com.lannstark.lec10

class Cat (
    species: String
) : Animal(species, 4) {  // extends 대신 : 을 사용한다. 단, 콜론 앞에 한칸띄워야된다
    override fun move() {
        println("Meow 사뿐사뿐")
    }
}