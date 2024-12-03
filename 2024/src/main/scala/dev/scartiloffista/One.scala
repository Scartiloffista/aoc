package dev.scartiloffista
import dev.scartiloffista.utils.ReadFile

@main def one() =
  val input = ReadFile.getLines(1)
  val numbers = input
    .map(_.split("\\s+").map(_.toInt).toSeq)
    .transpose
    .map(_.sorted)

  val res = numbers(0)
    .zip(numbers(1))
    .map { case (a, b) => Math.abs(Math.abs(a) - Math.abs(b)) }
    .sum

  println(res)

  // .map{ case Seq(a, b) => a + b }
  // .foreach(println)

@main def two() =
  val input = ReadFile.getLines(1)
  val numbers = input
    .map(_.split("\\s+").map(_.toInt).toSeq)
    .transpose
    .map(_.sorted)

  val freq = numbers(1).groupBy(identity).mapValues(_.size)

  val res = numbers(0)
    .map(c => c * freq.getOrElse(c, 0))
    .sum

  println(res)
