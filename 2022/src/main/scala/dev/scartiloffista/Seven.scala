package dev.scartiloffista

import utils.ReadFile

case class File(name: String, size: Int)

case class Node(name: String, var folders: Seq[Node], var files: Seq[File], parent: Option[Node], var size: Int = 0){
  override def toString() = s"Node($name)"
}

object Seven extends App {

  var targets: List[Node] = List[Node]()

  def navigate(node: Node): Int = {
//    println(s"visiting ${node.name}")

    var acc = 0
    for(child <- node.folders){
      acc += navigate(child)
    }

    acc += node.files.map(_.size).sum
    if(acc <= 100000)
      targets = targets :+ node

    node.size = acc
    acc
  }


  val root = Node("/", Nil, Nil, None)
  var current = root

  val input = ReadFile.getString("7")
  val sections = input.split("\n\\$").toList.map(_.split("\n").map(_.trim)).tail

  for(item <- sections){
    val command = item.head.split(" ")
    command.head match {
      case "ls" => {
        val files = item.tail.filter(_.split(" ").head != "dir").map(_.split(" ")).map(x => File(x(1), x(0).toInt))
        val folders = item.tail.filter(_.split(" ").head == "dir").map(x => Node(x.split(" ")(1), Nil, Nil, Some(current)))

        current.files = files
        current.folders = folders
      }
      case "cd" => {
        val folder = command(1)
        folder match {
          case ".." => current = current.parent.get
          case _ => current = current.folders.find(_.name == folder).get
        }
      }
    }
  }

  navigate(root)

  println(targets.map(_.size).sum)
}
