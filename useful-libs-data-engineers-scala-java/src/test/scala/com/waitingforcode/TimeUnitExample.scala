package com.waitingforcode

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

import java.util.concurrent.TimeUnit

class TimeUnitExample extends AnyFlatSpec with Matchers {

  "seconds" should "be converted to minutes and milliseconds with TimeUnit" in {
    val inputSeconds = 120

    TimeUnit.SECONDS.toMinutes(inputSeconds) shouldEqual 2
    TimeUnit.SECONDS.toMillis(inputSeconds) shouldEqual 120000
  }

}
