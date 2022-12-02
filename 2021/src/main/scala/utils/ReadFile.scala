package dev.scartiloffista
package utils

import scala.io.Source

object ReadFile {
  def getLines(n: Int): Seq[String] = {
    val source = Source.fromFile(s"inputs/$n.txt")
    val lines = try source.getLines().toSeq finally source.close()
    lines
  }
}
