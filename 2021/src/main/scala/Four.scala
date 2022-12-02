package dev.scartiloffista

import utils.ReadFile

import scala.collection.mutable.ListBuffer

object Four extends App {


  val instrs = ReadFile.getLines(4)

  val toDraws = instrs.head.split(",")

  var tables = instrs.tail.mkString("\n").split("\n\n")
    .map(_.trim)
    .map(_.split("\n"))
    .map(x => x.map(_.trim).map(_.split(" +")))

  def markNumbers(tables: Array[Array[Array[String]]], x: String) = {
    tables.map(row => row.map(item => item.map(s => if (s.equals(x)) s + "x" else s)))
  }

  def checkIfWin(tables: Array[Array[Array[String]]]) = {
    tables.filter(table => table.exists(row => row.mkString("").count(_ == 'x') == 5) ||
      (0 until 5).exists(i => table.count(row => row(i).contains("x")) == 5)
    )
  }

  val winsList = new ListBuffer[Int]
  for (x <- toDraws) {
    tables = markNumbers(tables, x)

    val wins = checkIfWin(tables)
    tables = tables.filter(
      table => !(table.exists(row => row.mkString("").count(_ == 'x') == 5) ||
        (0 until 5).exists(i => table.count(row => row(i).contains("x")) == 5)
        )
    )
    winsList.addAll(wins.map(win => win.flatten.filter(!_.endsWith("x")).map(_.toInt).sum * x.toInt))

  }
  winsList.foreach(println)
}
