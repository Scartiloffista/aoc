package dev.scartiloffista

import utils.ReadFile

import scala.annotation.tailrec

object Ten extends App {

  val input = ReadFile.getLines(10)
  val p1 = input.flatMap(x => fn(x, "")).sum
  val p2 = input.filter(x => fn(x, "").isEmpty).map(fn2(_, "", 0)).sorted
  val p2Res = p2(p2.length / 2)

  println(p1)
  println(p2Res)

  def scoringP1(head: Char): Int = Map(')' -> 3, ']' -> 57, '}' -> 1197, '>' -> 25137)(head)

  @tailrec
  def fn(str: String, open: String): Option[Int] = {
    val mapping = Map('(' -> ')', '[' -> ']', '{' -> '}', '<' -> '>')
    (str, open) match {
      case ("", _) => None
      case _ => str.head match {
        // no way to check if keys contain, i guess
        case strHead if mapping.keys.count(_ == strHead) > 0
          => fn(str.tail, mapping(strHead) + open)
        case strHead =>
          open.head match {
            case openHead if openHead.equals(strHead) => fn(str.tail, open.tail)
            case _ => Some(scoringP1(str.head))
        }
      }
    }
  }

  def scoringP2(open2: String): Long = open2.foldLeft(0L)((acc, char) => 5 * acc + Map(')' -> 1, ']' -> 2, '}' -> 3, '>' -> 4)(char))

  @tailrec
  def fn2(str: String, open: String, acc: Long): Long = {
    val mapping = Map('(' -> ')', '[' -> ']', '{' -> '}', '<' -> '>')
    (str, open) match {
      case ("", open2) => scoringP2(open2)
      case _ => str.head match {
        case foo if mapping.keys.count(_ == foo) > 0 => fn2(str.tail, mapping(foo) + open, acc)
        case _ => fn2(str.tail, open.tail, acc)
      }
    }
  }
}