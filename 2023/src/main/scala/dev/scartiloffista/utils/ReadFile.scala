package dev.scartiloffista.utils

import scala.io.Source

object ReadFile:
  def getLines(n: Int, example: Boolean = false): Seq[String] =
    val exampleString = example match
      case true  => ".example"
      case false => ""

    val source = Source.fromFile(s"inputs/$n.txt$exampleString")
    val lines =
      try source.getLines().toSeq
      finally source.close()
    lines
