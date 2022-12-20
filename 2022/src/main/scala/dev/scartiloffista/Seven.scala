package dev.scartiloffista

import utils.ReadFile

case class File(name: String, size: Int)

case class NodeDaySeven(
    name: String,
    var folders: Seq[NodeDaySeven],
    var files: Seq[File],
    parent: Option[NodeDaySeven],
    var size: Int = 0
) {
  override def toString = s"NodeDaySeven($name)"
}

object Seven extends App {

  var nodes: List[NodeDaySeven] = List[NodeDaySeven]()

  def navigate(node: NodeDaySeven): Int = {

    var acc = 0
    for (child <- node.folders) {
      acc += navigate(child)
    }

    acc += node.files.map(_.size).sum
    nodes = nodes :+ node
    node.size = acc
    acc
  }

  val root = NodeDaySeven("/", Nil, Nil, None)
  var current = root

  val input = ReadFile.getString("7")
  val sections = input.split("\n\\$").toList.map(_.split("\n").map(_.trim)).tail

  for (item <- sections) {
    val command = item.head.split(" ")
    command.head match {
      case "ls" =>
        val files = item.tail
          .filter(_.split(" ").head != "dir")
          .map(_.split(" "))
          .map(x => File(x(1), x(0).toInt))
        val folders = item.tail
          .filter(_.split(" ").head == "dir")
          .map(x => NodeDaySeven(x.split(" ")(1), Nil, Nil, Some(current)))

        current.files = files
        current.folders = folders
      case "cd" =>
        val folder = command(1)
        folder match {
          case ".." => current = current.parent.get
          case _    => current = current.folders.find(_.name == folder).get
        }
    }
  }

  navigate(root)

  // p1
  println(nodes.filter(_.size <= 100000).map(_.size).sum)

  // p2
  val occupiedSpace = root.size
  val currentFreeSpace = 70000000 - occupiedSpace
  val neededSpace = 30000000 - currentFreeSpace
  println(nodes.filter(_.size >= neededSpace).minBy(_.size).size)

}
