package com.lannstark.lec11

// bytecode 상에서는 static class가 생성되고 내부에 static method가 생성된다.
fun isDirectoryPath(path: String): Boolean {
    return path.endsWith("/")
}
