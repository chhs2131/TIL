package com.lannstark.lec07

import java.io.BufferedReader
import java.io.File
import java.io.FileReader

class FilePrinter {
    fun readFile() {  // kotlin에서는 모두 Unchecked Exception 이다.
        val currentFile = File(".")
        val file = File(currentFile.absoluteFile, "/a.txt")
        val reader = BufferedReader(FileReader(file))
        println(reader.readLine())
        reader.close()
    }

    // try with resources
    fun readFile(path: String) {
        BufferedReader(FileReader(path)).use {reader ->
            println(reader.readLine())
        }
    }
}