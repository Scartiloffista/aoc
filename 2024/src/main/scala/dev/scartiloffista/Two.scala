package dev.scartiloffista

import utils.ReadFile

object Two extends App:

  // format: off
  val kindaPermutations = (x: Seq[Int]) => { (0 until x.length).map(i => x.patch(i, Nil, 1)) }
  val first  = (x: Seq[Int]) => x.sliding(2).forall { case Seq(a, b) => a < b && Seq(1, 2, 3).contains(b - a) }
  val second = (x: Seq[Int]) => x.sliding(2).forall { case Seq(a, b) => a > b && Seq(1, 2, 3).contains(a - b) }
  val third  = (x: Seq[Int]) => first(x) || second(x) || kindaPermutations(x).exists(first) || kindaPermutations(x).exists(second)
  //format: on

  val p1 = (x: Seq[Int]) => first(x) || second(x)
  val p2 = third

  println(one())
  println(two())

  def one() =
    ReadFile
      .getLines(2, false)
      .map(_.split(" ").map(_.toInt).toSeq)
      .filter { p1 }
      .length

  def two() =
    ReadFile
      .getLines(2)
      .map(_.split(" ").map(_.toInt).toSeq)
      .filter { p2 }
      .length
