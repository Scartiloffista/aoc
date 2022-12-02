package dev.scartiloffista

import utils.ReadFile

object Twelve extends App {

  val startTimeMillis = System.currentTimeMillis()
  val input = ReadFile.getLines(12).map(_.split("-")).toArray.map { case Array(f1, f2) => (f1, f2) }
  val mapping = input ++ input.map(x => (x._2, x._1))

  def p1(mapping: Array[(String, String)], visited: Seq[String], node: String): Seq[Seq[String]] = {

    if (node.equals("end"))
      return Seq(Seq("end"))

    val neighs = mapping.filter(x => x._1.equals(node) && !visited.contains(x._2)).map(_._2)
    val newVisited = if (node.forall(_.isLower)) visited :+ node else visited
    var paths = Seq[Seq[String]]()

    if (neighs.isEmpty) {
      // can't continue
      return Seq[Seq[String]]()
    } else {
      for (x <- neighs) {
        val pathsBoh = p1(mapping, newVisited, x).filter(_.nonEmpty)
        paths = paths ++ pathsBoh.map(x => Seq(node) ++ x)
        //paths = paths (Seq(node) ++ p1(mapping, newVisited, x).getOrElse(paths.empty))
      }
    }
    paths
  }


  def p2(mapping: Array[(String, String)], visited: Seq[String], node: String, smallIsDone: Boolean): Seq[Seq[String]] = {

    if (node.equals("end"))
      return Seq(Seq("end"))
    val neighs = mapping.filter(x => x._1.equals(node) && !visited.contains(x._2)).map(_._2)



    var paths = Seq[Seq[String]]()
    if (neighs.isEmpty) {
      // can't continue
      return Seq[Seq[String]]()
    }

    if (smallIsDone){
      val newVisited = if (node.forall(_.isLower))
        visited :+ node
      else visited

      for (x <- neighs) {
        val pathsBoh = p2(mapping, newVisited, x, smallIsDone).filter(_.nonEmpty)
        paths = paths ++ pathsBoh.map(x => Seq(node) ++ x)
      }
      paths
    } else{
      // smallisdone false
      // prima come se nulla fosse
      for (x <- neighs) {

        val newVisited = if (node.forall(_.isLower))
          visited :+ node
        else visited

        val pathsBoh = p2(mapping, newVisited, x, smallIsDone = false).filter(_.nonEmpty)
        paths = paths ++ pathsBoh.map(x => Seq(node) ++ x)
      }

      if(node.forall(_.isLower)){
        for (x <- neighs) {
          val pathsBoh = p2(mapping, visited, x, smallIsDone = true).filter(_.nonEmpty)
          paths = paths ++ pathsBoh.map(x => Seq(node) ++ x)
          //paths = paths (Seq(node) ++ p1(mapping, newVisited, x).getOrElse(paths.empty))
        }
      }
      paths
    }
  }


  val res1 = p1(mapping, Seq("start"), "start")

  println(res1.size)

  val res2 = p2(mapping, Seq("start"), "start", smallIsDone = false).map(_.mkString(",")).toSet

  println(res2.size)
  val endTimeMillis = System.currentTimeMillis()
  val durationSeconds = endTimeMillis - startTimeMillis

  println(s"duration: $durationSeconds ms")

}
