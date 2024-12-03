package dev.scartiloffista

import utils.ReadFile

object Two extends App:

  // format: off
  val first  = (x: Seq[Int]) => x.sliding(2).forall { case Seq(a, b) => a < b && Seq(1, 2, 3).contains(b - a) }
  val second = (x: Seq[Int]) => x.sliding(2).forall { case Seq(a, b) => a > b && Seq(1, 2, 3).contains(a - b) }
  val kindaPermutations = (x: Seq[Int]) => { (0 until x.length).map(i => x.patch(i, Nil, 1)) }
  //format: on

  println(one())
  println(two())

  def one() =
    ReadFile
      .getLines(2, false)
      .map(_.split(" ").map(_.toInt).toSeq)
      .filter { x => first(x) || second(x) }
      .length

  def two() =
    ReadFile
      .getLines(2)
      .map(_.split(" ").map(_.toInt).toSeq)
      .filter { x => 
        //format: off
        first(x) || second(x) || kindaPermutations(x).exists(first) || kindaPermutations(x).exists(second)
        //format: on
      }
      .length
