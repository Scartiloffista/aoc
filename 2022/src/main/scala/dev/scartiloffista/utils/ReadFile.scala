package dev.scartiloffista
package utils

import scala.io.Source

object ReadFile {
  def getLines(n: String): Seq[String] = {
    val source = Source.fromFile(s"$n.txt")
    val lines = try source.getLines().toSeq finally source.close()
    lines
  }

  def getString(n: String): String = {
    val source = Source.fromFile(s"$n.txt")
    val lines: String = try source.mkString finally source.close()
    lines
  }
}
