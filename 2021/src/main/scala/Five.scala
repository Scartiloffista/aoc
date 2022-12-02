package dev.scartiloffista

import utils.ReadFile

import scala.collection.mutable.ListBuffer

object Five extends App {


  def getEquation(x1: Int, y1: Int, x2: Int, y2: Int): (Int, Int) => Boolean = {
    (x: Int, y: Int) => {
      val a = y2-y1
      val b = x1-x2
      val c = a*x1 + b*y1
      (a*x + b*y) == c &&
        (((x1 <= x) && (x <= x2)) || ((x2 <= x) && (x <= x1))) &&
        (((y1 <= y) && (y <= y2)) || ((y2 <= y) && (y <= y1)))
    }
  }

  def checkCovers(x: Int, y: Int, coordsP1: Seq[(Int, Int, Int, Int)]): Int = {
    coordsP1
      .map(x => getEquation(x._1, x._2, x._3, x._4))
      .map(fn => fn(x, y)).count(_ == true)
  }

  val lines = ReadFile.getLines(5)
  val regexp = """^(\d+),(\d+) -> (\d+),(\d+)$""".r
  val coords = lines.map{case regexp(x1,y1,x2,y2) => (x1.toInt, y1.toInt, x2.toInt, y2.toInt) }

  val max_x = (coords.map(_._1) ++ coords.map(_._3)).max
  val max_y = (coords.map(_._2) ++ coords.map(_._4)).max

  val coordsP1 = coords//.filter(c => c._1 == c._3 || c._2 == c._4)

  val covers = new ListBuffer[Int]

  for (x <- 0 to max_x){
    for(y <- 0 to max_y) {
      val nLinesCovering = checkCovers(x, y, coordsP1)
      covers.addOne(nLinesCovering)
    }
  }

  println(covers.count(_ >= 2))

}
