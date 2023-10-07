package com.lannstark.lec03

fun main() {
    val number1 = 3
    val number2: Long = number1.toLong()  // kotlin은 명시적으로 타입변환이 필요함

    val person = Person("a", 100)
    printAgeIfPerson2(person)

    // string format
    println("이름: ${person.name} 나이: ${person.age}")  // 중괄호는 생략하지 않는 것이 좋음

    // multi line String
    val string = """
        이름: ${person.name}
        나이: ${person.age}
    """.trimIndent()

    val abcd = "abcd"
    println(abcd[1])  // b
}

fun printAgeIfPerson(obj: Any) {
    if (obj is Person) {
//        val person = obj as Person
//        println(person.age)
        println(obj.age)  // smart cast: 문맥을 체크하여 타입을 자동으로 추론하기 때문에 가능함
    }
}

fun printAgeIfPerson2(obj: Any?) {
    val person = obj as? Person
    println(person?.age)  // null이 들어온경우 출력은 null
}
