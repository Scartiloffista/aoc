package dev.scartiloffista

object Three extends App:
  two()

  def two() =
    val input = utils.ReadFile.getLines(3).mkString("")
    val filtered = helper(input, Seq(), false).mkString("")
    println(one(filtered))

  def one(input: String) =
    val mulPattern = """mul\(\d+,\d+\)""".r
    val numPattern = """\d+""".r
    mulPattern
      .findAllIn(input)
      .map(_.toString())
      .map(numPattern.findAllIn(_).map(_.toInt))
      .map(_.product)
      .sum

  def helper(s: String, acc: Seq[String], ignore: Boolean): Seq[String] =

    if s.isEmpty then return acc

    val d0 = s.split("do\\(\\)", 2)
    val d0nt = s.split("don\\'t\\(\\)", 2)

    val (toUse, newIgnore) =
      // format: off
      if d0(0).length() > d0nt(0).length() then (d0nt.toSeq, true)
      else (d0.toSeq, false) // if do1 is a bigger list, means that the don't comes first
      // format: on
    val newAcc = if ignore then acc else acc :+ toUse(0)

    if toUse.length > 1 then return helper(toUse(1), newAcc, newIgnore)
    else return newAcc
