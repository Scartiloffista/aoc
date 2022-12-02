package dev.scartiloffista

import utils.ReadFile

object One extends App {
  val nums = ReadFile.getLines(1).map(_.toInt)
  val res = nums.zip(nums.drop(3)).map(t => t._2 > t._1).count(_ == true)

  println(res)
}
