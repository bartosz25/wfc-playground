package com.waitingforcode

import org.apache.commons.io.FileUtils
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

import java.io.File
import java.util.concurrent.{CountDownLatch, TimeUnit}

class CountDownLatchExample extends AnyFlatSpec with Matchers {

  "CountDownLatch" should "coordinate 2 processes" in {
    val textToWrite =
      """
        |line#1
        |line#2
        |line#3
        |""".stripMargin

    val countDownLatch = new CountDownLatch(1)
    new Thread(new Runnable() {
      override def run(): Unit = {
        // Give some time to see the synchronization
        Thread.sleep(3000L)
        try {
          FileUtils.writeStringToFile(new File("/tmp/test.txt"), textToWrite, "UTF-8")
        } finally {
          countDownLatch.countDown()
        }
      }
    }).start()

    println("Doing some other, more important work here")

    countDownLatch.await(10, TimeUnit.SECONDS)

    FileUtils.readFileToString(new File("/tmp/test.txt"), "UTF-8") shouldEqual textToWrite
  }

}
