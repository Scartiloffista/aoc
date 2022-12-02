package dev.scartiloffista

import utils.ReadFile

object Two extends App {
  val regexp = """^(.*) (.*)$""".r
  val instrs = ReadFile.getLines(2).map { case regexp(dir, n) => (dir, n.toInt) }

  val foo = instrs.foldLeft((0, 0)) {
    case ((pos, dep), (dir, n)) =>
      dir match {
        case "up" => (pos, dep - n)
        case "down" => (pos, dep + n)
        case "forward" => (pos + n, dep)
      }
  }

  val res = foo._1 * foo._2
  println(res)

  val foo2 = instrs.foldLeft((0, 0, 0)) {
    case ((pos, dep, aim), (dir, n)) =>
      dir match {
        case "up" => (pos, dep, aim - n)
        case "down" => (pos, dep, aim + n)
        case "forward" => (pos + n, dep + (aim * n), aim)
      }
  }
  val res2 = foo2._1 * foo2._2
  println(res2)

}
