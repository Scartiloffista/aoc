package dev.scartiloffista

import dev.scartiloffista.utils.ReadFile

trait Coord(val x: Int, val y: Int)

case class Sensor(override x: Int, y: Int) extends Coord(x, y)
case class Beacon (x: Int, y: Int) extends Coord(x, y)


object Fifteen extends App {
  val input = ReadFile.getLines("15")

  val (bLis: Seq[Beacon], sList: Seq[Sensor]) = input.map(parseLine).unzip
  val beacons = bLis.toSet
  val sensors = sList.toSet



  def taxiDistance(s: Coord, b: Coord) = {
    Math.abs(s.x - b.x) + Math.abs(s.y - b.y)
  }

  def parseLine(line: String) = {
    val coords = line
      .replace("Sensor at ", "")
      .replace(": closest beacon is at ", ", ")
      .split(",")
      .grouped(2)
      .toSeq
      .map(_.map(_.split("=")(1).toInt))

    val b = Beacon(coords(1)(0), coords(1)(1))
    val s = Sensor(coords(0)(0), coords(0)(1))
    (b,s)

  }
}
