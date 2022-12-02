package dev.scartiloffista

import utils.ReadFile

import scala.annotation.tailrec

object Three extends App {

  def createMask(s: Seq[String]): Array[Int] = {
    // count instances for every pos in str
    s.foldLeft(new Array[Int](s.head.length)) { (acc, str) =>
      str
        .map(s => if (s == '0') -1 else 1).toArray
        .zip(acc)
        .map(x => x._1 + x._2)
    }
  }

  @tailrec
  def getOxygen(instrs: Seq[String], i: Int): Int = {
    val mask2 = createMask(instrs)
    val maskOxygen = mask2
      .map(_ >= 0)
      .map(if (_) 1 else 0)

    val filtered = instrs
      .filter(x => x(i).toString.toInt == maskOxygen(i))

    filtered.length match {
      case 1 => Integer.parseInt(filtered.head, 2)
      case _ => getOxygen(filtered, i + 1)
    }
  }

  @tailrec
  def getCO2(instrs: Seq[String], i: Int): Int = {
    val mask2 = createMask(instrs)
    val maskCO2 = mask2
      .map(_ < 0)
      .map(if (_) 1 else 0)

    val filtered = instrs.filter(x => x(i).toString.toInt == maskCO2(i))
    filtered.length match {
      case 1 => Integer.parseInt(filtered.head, 2)
      case _ => getCO2(filtered, i + 1)
    }
  }

  val instrs = ReadFile.getLines(3)
  val len = instrs.head.length

  val vals = createMask(instrs)
  val gammaStr = vals.foldLeft("")((s, c) => if (c > 0) s + "1" else s + "0")
  val epsilonStr = gammaStr.map(x => (1 - x.toString.toInt).toString).mkString("")
  val epsilon = Integer.parseInt(epsilonStr, 2)
  val gamma = Integer.parseInt(gammaStr, 2)

  val oxygen = getOxygen(instrs, 0)
  val CO2 = getCO2(instrs, 0)

  println(epsilon * gamma)
  println(CO2 * oxygen)

}
