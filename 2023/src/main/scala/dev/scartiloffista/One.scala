package dev.scartiloffista

import dev.scartiloffista.utils.ReadFile

val lines = ReadFile.getLines(1)

def p1: Int =
  val linesDigits = lines.map { l => l.filter(_.isDigit) }
  val numbers = linesDigits.map { l => 10 * (l.head - '0') + l.last - '0' }
  numbers.sum

def p2: Int = lines.map(findIndexOfNumber).sum

def findIndexOfNumber(s: String): Int =
  val mapNumbers = Map(
    "one" -> '1',
    "two" -> '2',
    "three" -> '3',
    "four" -> '4',
    "five" -> '5',
    "six" -> '6',
    "seven" -> '7',
    "eight" -> '8',
    "nine" -> '9'
  )

  val firstRealNumber = s.zipWithIndex.find((c, i) => c.isDigit)
  val lastRealNumber = s.zipWithIndex.find((c, i) => c.isDigit)

  val withLetters =
    Seq(
      "one",
      "two",
      "three",
      "four",
      "five",
      "six",
      "seven",
      "eight",
      "nine"
    ).flatMap { number =>
      val matchh = number.r.findAllIn(s)
      if matchh.nonEmpty then
        val indexes = matchh.matchData.map { m => m.start }.toList
        val min = indexes.min
        val max = indexes.max
        Seq(
          (mapNumbers(number), min),
          (mapNumbers(number), max)
        )
      else Nil
    }.distinct

  val seq = withLetters ++ Seq(firstRealNumber, lastRealNumber).flatten
  val first = seq.minBy(_._2)._1
  val last = seq.maxBy(_._2)._1

  10 * (first - '0') + last - '0'

@main def run(): Unit =
  println(p1)
  println(p2)
