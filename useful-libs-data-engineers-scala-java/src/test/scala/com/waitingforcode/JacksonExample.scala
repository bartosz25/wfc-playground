package com.waitingforcode

import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.module.scala.DefaultScalaModule
import org.apache.commons.io.FileUtils
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

import java.io.File

class JacksonExample extends AnyFlatSpec with Matchers {

  "ObjectMapper" should "write and read back a case class from file" in {
    val scalaJsonMapper = new ObjectMapper()
    scalaJsonMapper.registerModule(DefaultScalaModule)

    val personToSave = Person("Save", "Me")

    val personJson = scalaJsonMapper.writeValueAsString(personToSave)
    FileUtils.writeStringToFile(new File("/tmp/test.txt"), personJson, "UTF-8")

    scalaJsonMapper.readValue(new File("/tmp/test.txt"), classOf[Person]) shouldEqual personToSave
  }

}

case class Person(firstName: String, lastName: String)
