package dev.scartiloffista

object Seven extends App {

  val hP = utils.ReadFile.getLines(7).head.split(",").map(_.toInt).toList.sorted

  println(hP.map(x => (x - hP(hP.length / 2)).abs).sum)
  println(hP.map(x => hP.map(y => (y - x).abs * ((y - x).abs + 1) / 2).sum).min)

  val min = hP.min
  val max= hP.min

}