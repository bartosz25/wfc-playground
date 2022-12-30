package com.waitingforcode

import com.google.common.collect.Maps
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class MapsDifferencExample extends AnyFlatSpec with Matchers {

  "Maps.difference" should "show the exact mismatched keys for 2 compared maps" in {
    val mapLeft = new java.util.HashMap[String, Any]()
    mapLeft.put("common_equal", 1)
    mapLeft.put("common_different", 1)
    mapLeft.put("extra_in_left", "22222")
    val nestedMapLeft = new java.util.HashMap[String, Int]()
    nestedMapLeft.put("extra_left", 1)
    nestedMapLeft.put("common_equal", 2)
    mapLeft.put("different_nested_map", nestedMapLeft)

    val mapRight = new java.util.HashMap[String, Any]()
    mapRight.put("common_equal", 1)
    mapRight.put("common_different", 11)
    mapRight.put("extra_in_right", "33333")
    val nestedMapRight = new java.util.HashMap[String, Int]()
    nestedMapRight.put("extra_right", 11)
    nestedMapRight.put("common_equal", 2)
    mapRight.put("different_nested_map", nestedMapLeft)

    val diff = Maps.difference[String, Any](mapLeft, mapRight)

    diff.areEqual() shouldEqual false
    // {common_different=(1, 11)}
    println(diff.entriesDiffering())
    // {extra_in_left=22222}
    println(diff.entriesOnlyOnLeft())
    // {extra_in_right=33333}
    println(diff.entriesOnlyOnRight())
  }

}
