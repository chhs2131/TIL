package com.lannstark.lec14

// DTO를 위한 타입 data
// builder, equals, hashcode, toString 모두 자동생성됨
data class PersonDto(
    private val name: String,
    private val age: Int
)
