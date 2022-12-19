package dev.scartiloffista

import dev.scartiloffista.utils.ReadFile

import scala.collection.mutable

case class Monkey(
    number: Int,
    items: Seq[BigInt],
    op: BigInt => BigInt,
    modulo: Int,
    ifTrue: Int,
    ifFalse: Int
)

object Eleven extends App {

  val input = ReadFile.getString("11")
  val monkeysS = input.split("\n\n")

  val monkeys = monkeysS.map(fromStringToMonkey).map(m => (m.number, m)).toMap

  val counter = run(monkeys)

  val resultP1 =
    counter.values.toSeq.sorted.reverse.take(2).map(BigInt(_)).product
  println(resultP1)

  def run(monkeys: Map[Int, Monkey]) = {

    val allModulo = monkeys.values.map(_.modulo).product

    val counter = mutable.Map[Int, Int]()

    var monkeysVar = monkeys

    // iterations
    for (_ <- 0 until 10000) {

      // every monkey
      for (m <- 0 until monkeys.size) {
        val monkey = monkeysVar(m)

        // every item
        for (item <- monkey.items) {

          val worryLevel = monkey.op(item)

          if (worryLevel % monkey.modulo == 0) {
            val receiver = monkeysVar(monkey.ifTrue)
            monkeysVar = monkeysVar + (monkey.ifTrue -> receiver.copy(items =
              receiver.items :+ worryLevel % allModulo
            ))
          } else {
            val receiver = monkeysVar(monkey.ifFalse)
            monkeysVar = monkeysVar + (monkey.ifFalse -> receiver.copy(items =
              receiver.items :+ worryLevel % allModulo
            ))
          }
        }
        counter(monkey.number) =
          counter.getOrElse(monkey.number, 0) + monkey.items.size
        monkeysVar =
          monkeysVar + (monkey.number -> monkey.copy(items = Seq[BigInt]()))
      }
    }

    counter
  }

  def fromStringToMonkey(string: String) = {
    val lines = string.split("\n")

    val monkeyNumber = lines(0).split(" ").last.trim.takeWhile(_ != ':').toInt
    val startingItems =
      lines(1).split("Starting items: ").last.trim.split(", ").map(BigInt(_))

    // handling operation

    val operation =
      lines(2).split("Operation: new = old ").last.split(" ") match {
        case Array("*", "old") => (x: BigInt) => x * x
        case Array("+", "old") => (x: BigInt) => x + x
        case Array("+", y)     => (x: BigInt) => x + BigInt(y)
        case Array("*", y)     => (x: BigInt) => x * BigInt(y)
      }


    val modulo = lines(3).split(" ").last.trim.toInt
    val ifTrue = lines(4).split(" ").last.trim.toInt
    val ifFalse = lines(5).split(" ").last.trim.toInt

    Monkey(
      monkeyNumber,
      startingItems,
      operation,
      modulo,
      ifTrue,
      ifFalse
    )
  }
}
