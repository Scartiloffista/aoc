package dev.scartiloffista

import dev.scartiloffista.utils.ReadFile

object Four extends App:

  val input = ReadFile.getLines(4, false)

  val normal = Seq(
    input,
    rotation(input),
    rotation(rotation(input)),
    rotation(rotation(rotation(input)))
  ).map(_.map(_.sliding(4).count(_ == "XMAS")).sum).sum

  val diagonal = (0 until input(0).length - 3)
    .map { i =>
      (0 until input.length - 3).map { j =>

        val firstDiag = Seq(
          input(j + 3)(i),
          input(j + 2)(i + 1),
          input(j + 1)(i + 2),
          input(j)(i + 3)
        ).mkString

        val secondDiag =
          Seq(
            input(j)(i),
            input(j + 1)(i + 1),
            input(j + 2)(i + 2),
            input(j + 3)(i + 3)
          ).mkString

        Seq(
          secondDiag == "XMAS",
          secondDiag == "SAMX",
          firstDiag == "XMAS",
          firstDiag == "SAMX"
        ).count(_ == true)

      }
    }
    .flatten
    .sum

  val p1 = normal + diagonal

  val p2 = (0 until input(0).length - 2)
    .map { i =>
      (0 until input.length - 2).map { j =>

        val firstDiag = Seq(
          input(j + 2)(i),
          input(j + 1)(i + 1),
          input(j)(i + 2)
        ).mkString

        val secondDiag =
          Seq(
            input(j)(i),
            input(j + 1)(i + 1),
            input(j + 2)(i + 2)
          ).mkString

        Seq(
          (secondDiag == "MAS" ||
            secondDiag == "SAM") &&
            (firstDiag == "MAS" ||
              firstDiag == "SAM")
        ).count(_ == true)

      }
    }
    .flatten
    .sum

  println(p1)
  println(p2)

  def rotation(list: Seq[String]) = list.transpose.map(_.reverse.mkString)
