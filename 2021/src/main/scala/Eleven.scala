package dev.scartiloffista

import utils.ReadFile

import scala.annotation.tailrec
import scala.language.postfixOps

object Eleven extends App {

  val input = ReadFile.getLines(11).map(_.split("").map(_.toInt))

  val indices = input.indices.flatMap(y => input.head.indices.map(x => (x, y) -> input(y)(x))).toMap
  val res1 = p1(indices, 0, 0)
  println(res1)

  def getNeigh(p: (Int, Int), input: Map[(Int, Int), Int]) = {
    Seq(-1, 0, 1).flatMap(x => Seq(-1, 0, 1).map(y => (x, y))).filter(x => x != (0, 0))
      .map(x => (p._1 + x._1, p._2 + x._2))
      .filter(x => input.contains(x))
  }

  @tailrec
  def expand(input: Map[(Int, Int), Int], glowing: Set[(Int, Int)], toIgnore: Set[(Int, Int)]): Map[(Int, Int), Int] = {

    if (glowing.isEmpty)
      return input

    val neigh = glowing.toSeq.flatMap(x => getNeigh(x, input))
    val step = neigh.foldLeft(input)((step, x) => step + (x -> (step(x) + 1)))
    val glowed = toIgnore concat glowing
    val newGlowing = step.filter(_._2 > 9).filter(x => !glowed.contains(x._1)).keys.toSet

    if (newGlowing.nonEmpty)
      expand(step, newGlowing, glowed)
    else
      step
  }

  @tailrec
  def p1(input: Map[(Int, Int), Int], step: Int, acc: Long): Long = {
    if (step == 100) // set to high for p2
      acc
    else {
      val firstStep = input map { case (k, v) => k -> (v + 1) }
      val glowing = firstStep filter (_._2 > 9) keys
      val secondStep = expand(firstStep, glowing.toSet, glowing.toSet.empty)
      val count = secondStep.count(_._2 > 9)
      val finalStep = secondStep.map { case (k, v) => k -> (if (v <= 9) v else 0) }

      if (finalStep.forall(x => x._2 == 0)) // for a stupid p2
        println(s"STEP: $step")
      p1(finalStep, step + 1, acc + count)
    }
  }
}
