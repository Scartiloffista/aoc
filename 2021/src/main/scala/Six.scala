package dev.scartiloffista

import utils.ReadFile

import scala.annotation.tailrec

object Six extends App {

  def generateDict(dict: Map[Int, Long]): Map[Int, Long] = {
    val foo = dict.map(x => x._1 - 1 -> x._2)
    val foo1 = foo + (8 -> foo.getOrElse(8, 0L).+(foo.getOrElse(-1, 0L)))
    val foo2 = foo1 + (6 -> foo1.getOrElse(6, 0L).+(foo1.getOrElse(-1, 0L)))
    val foo3 = foo2 - -1
    foo3
  }

  @tailrec
  def iterateDict(dict: Map[Int, Long], day: Int): Long = {
    day match {
      case 0 => dict.values.sum
      case _ => iterateDict(generateDict(dict), day - 1)
    }
  }

  val input = ReadFile.getLines(6).head.split(",").map(_.toInt)
  val dict = (0 to 8).map { x => x -> input.count(y => y == x).toLong }.toMap

  val result1 = iterateDict(dict, 80)
  val result2 = iterateDict(dict, 256)

  println(result1)
  println(result2)

}