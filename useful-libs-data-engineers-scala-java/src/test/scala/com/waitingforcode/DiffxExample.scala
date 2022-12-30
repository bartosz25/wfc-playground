package com.waitingforcode

import com.softwaremill.diffx.generic.auto._
import com.softwaremill.diffx.scalatest.DiffShouldMatcher
import com.softwaremill.diffx.scalatest.DiffShouldMatcher._
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class DiffxExample extends AnyFlatSpec with Matchers with DiffShouldMatcher {

  behavior of "case class comparison"

  it should "print no differences without Diffx" in {
    val letter = Letter(1, "a", "AA")

    letter shouldEqual Letter(1, "a", "A")
  }

  it should "print differences with Diffx" in {
    val letter = Letter(1, "a", "AA")

    letter shouldMatchTo Letter(1, "a", "A")
  }

}

case class Letter(id: Int, lower: String, upper: String)