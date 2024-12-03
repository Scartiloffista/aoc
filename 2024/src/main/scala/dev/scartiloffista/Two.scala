package dev.scartiloffista

import utils.ReadFile

object Two extends App:

  println(one())
  println(two())

  def one() =
    ReadFile
      .getLines(2, false)
      .map(_.split(" ").map(_.toInt).toSeq)
      .filter { list =>
        // format: off
        list.sliding(2).forall { case Seq(a, b) => a < b && Seq(1,2,3).contains(b-a) } || list.sliding(2).forall { case Seq(a, b) => a > b && Seq(1,2,3).contains(a-b) }
        //format: on

      }
      .length

  def two() =
    // format: off

    val first  = (x: Seq[Int]) => x.sliding(2).forall { case Seq(a, b) => a < b && Seq(1, 2, 3).contains(b - a) }
    val second = (x: Seq[Int]) => x.sliding(2).forall { case Seq(a, b) => a > b && Seq(1, 2, 3).contains(a - b) }
    
    val kindaPermutations = (x: Seq[Int]) => { (0 until x.length).map(i => x.patch(i, Nil, 1)) }

    ReadFile
      .getLines(2)
      .map(_.split(" ").map(_.toInt).toSeq)
      .filter { list =>
        first(list) || second(list) || kindaPermutations(list).exists(first) || kindaPermutations(list).exists(second)
      }.length