package dev.scartiloffista

import utils.ReadFile

object Eight extends App:

  val lines = ReadFile.getLines(8)
  val fullInstructions = lines(0)
  val mapp = lines
    .drop(2)
    .map { command =>
      val s"${x} = (${y}, ${z})" = command
      (x, (y, z))
    }
    .toMap

  one()
  two()

  def two() =
    val starting = mapp.keys.filter(_.endsWith("A"))
    println(starting)
    val lenghts = starting.map(x => helper(fullInstructions, x, 0))
    lenghts.foreach(println)
    // print(lenghts)

  def helper(instrs: String, curr: String, acc: Int): Int =
    val currentInstrs = if instrs.nonEmpty then instrs else fullInstructions

    if curr.endsWith("Z") then return acc
    else
      val nextCurr =
        if currentInstrs(0) == 'L' then mapp(curr)._1 else mapp(curr)._2

      return helper(currentInstrs.tail, nextCurr, acc + 1)

  def one() =
    val countt = helper(fullInstructions, "AAA", 0)
    println(countt)

  import scala.math._

  def lcm(a: Int, b: Int): Int = abs(a * b) / (BigInt(a).gcd(b).toInt)

  def lcmOfList(numbers: List[Int]): Int = {
    numbers.foldLeft(1)(
      lcm
    ) // Starts with 1 and iteratively computes the LCM of the list
  }
