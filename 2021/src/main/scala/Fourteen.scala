package dev.scartiloffista

import utils.ReadFile

import scala.annotation.tailrec

object Fourteen extends App {

  val input = ReadFile.getLines(14).mkString("\n")
  val startString = input.split("\n\n").head

  val rules: Map[String, String]     = input.split("\n\n")(1).split("\n").map(x => x.split(" -> ")).map(x => x(0) -> x(1)).toMap
  val occurrences: Map[String, Long] = startString.sliding(2).map(x => x -> startString.sliding(2).toList.count(_ == x).toLong).toMap
  val finalMap: Map[String, Long]    = newP2(occurrences, rules, 1)
  val charCount: Map[Char, Long]     = finalMap.groupBy(_._1(1)).view.mapValues(_.values.sum).toMap // counting only second letter of final pairs

  println(charCount.values.max - charCount.values.min)

  @tailrec
  def newP2(stringMap: Map[String, Long], rules: Map[String, String], i: Int): Map[String, Long] = {
    if (i > 40)
      return stringMap

    val foo = stringMap.toSeq.flatMap { case (pair, count) =>
      val (a, b, c) = (pair(0), pair(1), rules(pair))
      Seq((a + c, count), (c + b, count)) // from a pair, spawning two of them
    }.groupBy(_._1).view.mapValues(_.map(_._2).sum).toMap // grouping by pair and sum occurrences

    newP2(foo, rules, i + 1)
  }
}
