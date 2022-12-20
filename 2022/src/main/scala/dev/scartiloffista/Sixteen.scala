package dev.scartiloffista

import dev.scartiloffista.utils.ReadFile
import scala.collection.mutable

case class Node(name: String, flow: Int, edges: Seq[String])

object Sixteen extends App {

  val input = ReadFile.getLines("16.example")

  val nodes: Set[Node] = input.map(parseLine).toSet

  val starting = nodes.filter(_.name == "AA").head

  val memo = mutable.Map[(Node, Set[Node], Int), (Int, Set[Node])]()

  val foo = buildMatrix(starting, Set.empty, 30)

  println(foo._2.map(_.name))

  println(foo._1)

  def buildMatrix(
      current: Node,
      open: Set[Node],
      minute: Int
  ): (Int, Set[Node]) = {

    if (minute <= 0) {
      return (0, open)
    }

    val candidates: Set[(Node, Set[Node], Int)] = nodes
      .filter(n => current.edges.contains(n.name))
      .map((_, open, minute - 1))

    val sureCandidates: Set[(Int, Set[Node])] = candidates.map {
      case (n, o, m) => handleMemo(n, o, m)
    } ++
      (if ((current.flow == 0 || open.contains(current))) {
         Set[(Int, Set[Node])]()
       } else {
         candidates.map {
           case (n, o, m) => {
             val foo = handleMemo(n, o + current, m - 1)
             (foo._1 + current.flow * minute, foo._2)
           }
         }
       })

    if (minute == 30)
      println(sureCandidates)

    val foo = sureCandidates.toList.maxBy(_._1)

    foo

//    {
//      case (n, o, m) => {
//        if (memo.contains((n, o, m))) {
//          memo((n, o, m))
//        } else {
//          buildMatrix(n, o, m)
//        }
//      }
//    }

//    val sureCandidates: Set[Int] = candidates.map {
//      case (n, o, m) => {
//        if (memo.contains((n, o, m))) {
//          memo((n, o, m))
//        } else {
//          buildMatrix(n, o, m)
//        }
//      }
//    }

//    if (current.flow == 0 || open.contains(current)) {
//
//      candidates.map {
//        case (n, o, m) => {
//          if (memo.contains((n, o, m))) {
//            memo.get((n, o, m))
//          } else {
//            buildMatrix(n, o, m)
//          }
//        }
//      }
//
//      nextPossibleNodes
//        .map(n => buildMatrix(n, open, minute + 1))
//        .reduce(_ ++ _)
//
//    } else {
//      nextPossibleNodes
//        .map(n => buildMatrix(n, open, minute + 1))
//        .reduce(_ ++ _) ++
//        nextPossibleNodes
//          .map(n =>
//            buildMatrix(
//              n,
//              open + current,
//              actualFlow + (minute + current.flow),
//              minute + 2,
//              nodes
//            )
//          )
//          .reduce(_ ++ _)reduce
//    }

  }

  private def handleMemo(n: Node, o: Set[Node], m: Int) = {
    if (!memo.contains((n, o, m))) {
      memo.put((n, o, m), buildMatrix(n, o, m))
    }

    memo((n, o, m))
  }

  def parseLine(s: String) = {
    val name = s.split(" ")(1)
    val flow = s.split(";")(0).split("=")(1).toInt
    val edges = s.contains("valves") match {
      case true  => s.split(" tunnels lead to valves ")(1).split(", ").toSeq
      case false => Seq(s.split(" tunnel leads to valve ")(1))
    }

    Node(name, flow, edges)
  }
}
