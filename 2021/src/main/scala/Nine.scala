package dev.scartiloffista

import utils.ReadFile

import scala.collection.immutable.Queue
import scala.language.postfixOps

object Nine extends App {

  val input: Seq[Array[Int]]        = ReadFile.getLines(9).map(_.split("")).map(_.map(_.toInt))
  val indices: Map[(Int, Int), Int] = input.indices.flatMap(y => input.head.indices.map(x => ((x, y), input(y)(x)))).toMap
  val mins: Map[(Int, Int), Int]    = indices.filter(x => findAMin(x, indices))

  val p1 = mins.map(_._2 + 1).sum
  val p2 = mins.map(x => bfs(x._1, indices)).toList.sorted.reverse.slice(0, 3).product

  println(p1)
  println(p2)

  def findAMin(i: ((Int, Int), Int), indices: Map[(Int, Int), Int]): Boolean = {
    val (x, y) = i._1
    val v = i._2

    Seq((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)).map(x => indices.getOrElse(x, Int.MaxValue) > v).forall(_ == true)
  }

  def bfs(start: (Int, Int), indices: Map[(Int, Int), Int]) = {
    var mappingVisited = indices.map(x => x._1 -> true) + (start -> false)

    var queue: Queue[(Int, Int)] = Queue(start)

    while (queue.nonEmpty) {
      val pos = queue.dequeue
      queue = pos._2
      val (x, y) = pos._1

      for (dir <- Seq((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))) {
        if (mappingVisited.getOrElse(dir, false) && indices(dir) != 9) {
          queue = queue.enqueue(dir)
          mappingVisited = mappingVisited + (dir -> false)
        }
      }
    }
    mappingVisited.values.count(_ == false)
  }
}
