package dev.scartiloffista

import utils.ReadFile

object Eight extends App {

  val input = ReadFile.getLines(8)

  def fn(x: String) = {
    val foo    = x.split(""" \| """, 2)
    val signal = foo(0).split(" ").map(_.sorted)
    val value  = foo(1).split(" ").map(_.sorted)

    // uniques
    val one   = signal.filter(_.length == 2).head
    val four  = signal.filter(_.length == 4).head
    val seven = signal.filter(_.length == 3).head
    val eight = signal.filter(_.length == 7).head

    // |x| == 6
    val nine = signal.filter(x => x.length == 6 && x.intersect(four).length == 4 && x.intersect(seven).length == 3).head
    val zero = signal.filter(x => x.length == 6 && x != nine && x.intersect(one).length == 2).head
    val six  = signal.filter(x => x.length == 6 && x != nine && x != zero).head

    // |x| == 5
    val three = signal.filter(x => x.length == 5 && x.intersect(one).length == 2).head
    val five  = signal.filter(x => x.length == 5 && x.intersect(nine).length == 5 && x != three).head
    val two   = signal.filter(x => x.length == 5 && x != five && x != three).head


    val mapping = Map(
      one -> 1,
      two -> 2,
      three -> 3,
      four -> 4,
      five -> 5,
      six -> 6,
      seven -> 7,
      eight -> 8,
      nine -> 9,
      zero -> 0
    )

    val result = value.map(x=> mapping(x))
    result
  }

  val results = input.map(x => fn(x))

  val p1 = results.map(_.count(x=> x == 1 || x == 4 || x == 7 || x == 8)).sum
  val p2 = results.map(x => x.mkString("").toInt).sum

  println(p1)
  println(p2)

}
