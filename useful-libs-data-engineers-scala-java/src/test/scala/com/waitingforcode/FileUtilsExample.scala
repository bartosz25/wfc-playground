package com.waitingforcode

import org.apache.commons.io.FileUtils
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

import java.io.File

class FileUtilsExample extends AnyFlatSpec with Matchers {

  "FileUtils" should "write a string into file" in {
    val textToWrite =
      """
        |line#1
        |line#2
        |line#3
        |""".stripMargin

    FileUtils.writeStringToFile(new File("/tmp/test.txt"), textToWrite, "UTF-8")

    FileUtils.readFileToString(new File("/tmp/test.txt"), "UTF-8") shouldEqual textToWrite
  }

}
