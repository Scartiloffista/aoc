package dev.scartiloffista

import dev.scartiloffista.utils.ReadFile
import scala.collection.mutable

case class Node(name: String, flow: Int, edges: Seq[String])

object Sixteen extends App {

  val input = ReadFile.getLines("16")

  val nodes: Set[Node] = input.map(parseLine).toSet

  val starting = nodes.filter(_.name == "AA").head

  val memo = mutable.Map[(Node, Set[Node], Int, Boolean), Int]()

  print(buildMatrix(starting, Set.empty, 30, false))
  print(buildMatrix(starting, Set.empty, 26, true))

  def buildMatrix(
      current: Node,
      open: Set[Node],
      minute: Int,
      repeat: Boolean
  ): Int = {

    // finishing or restarting for the elephant?
    if (minute <= 0) {
      if(!repeat) {
        return 0
      }
      else {
        return buildMatrix(starting, open, 26, false)
      }
    }

    // where i can go, with new status
    val candidates: Set[(Node, Set[Node], Int)] = nodes
      .filter(n => current.edges.contains(n.name))
      .map((_, open, minute - 1))

    // results for candidates
    val sureCandidates: Set[Int] = candidates.map { case (n, o, m) =>
      handleMemo(n, o, m, repeat)
    } ++
    // if i have 0 flow or already open, i don't have to add anything
      (if ((current.flow == 0 || open.contains(current))) {
         Set.empty
       } else {
        // otherwise take into account also the opening of the current one
         candidates.map {
           case (n, o, m) => {
               handleMemo(n, o + current, m - 1, repeat) + current.flow * (minute - 1)
           }
         }
       })

   sureCandidates.max

  }

  private def handleMemo(n: Node, o: Set[Node], m: Int, repeat: Boolean): Int = {
    if (!memo.contains((n, o, m, repeat))) {
      memo.put((n, o, m, repeat), buildMatrix(n, o, m, repeat))
    }
    memo((n, o, m, repeat))
  }

  def parseLine(s: String): Node = {
    val name = s.split(" ")(1)
    val flow = s.split(";")(0).split("=")(1).toInt
    val edges = s.contains("valves") match {
      case true  => s.split(" tunnels lead to valves ")(1).split(", ").toSeq
      case false => Seq(s.split(" tunnel leads to valve ")(1))
    }

    Node(name, flow, edges)
  }
}
