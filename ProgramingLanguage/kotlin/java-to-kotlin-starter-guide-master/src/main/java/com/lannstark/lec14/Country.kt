package com.lannstark.lec14

fun handleCountry(country: Country): String {
    return when (country) {
        Country.KOREA -> "KO"
        Country.AMERICA -> "US"
    }
}

enum class Country(
    private val code: String,
) {
    KOREA("KO"),
    AMERICA("US")
    ;
}
