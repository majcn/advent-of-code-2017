import scala.io.Source

object Application {

  def readLines() = {
    Source.fromFile("1.input").getLines()
  }

  def main(args: Array[String]): Unit = {
    val line = readLines().next

    // println {
    //     line indices zipWithIndex filter { (l, i) => l == line((i + line.length / 2) % line.length } map { (l, _) => l.asDigit }
    // }


    // println {
    //     line zip (line.tail + line.head) filter { case (a, b) => a == b } map { case (v, _) => v.asDigit } sum
    // }


    // val zf2 = for { i <- 0 until line.length if line(i) == line((i + line.length / 2) % line.length) } yield line(i).asDigit
    // val result2 = zf2.sum

    // var result2 = 0
    // for (i <- 0 until line.length) {
    //     if (line(i) == line((i + line.length / 2) % line.length)) {
    //         result2 += line(i).asDigit
    //     }
    // }

    println {
        (line.zip(line.tail + line.head) filter { case (a, b) => a == b } map { _._1.asDigit }).sum
    }

    println {
        (line.zipWithIndex filter { case (a, i) => a == line((i + line.length / 2) % line.length) } map { _._1.asDigit }).sum
    }
  }
}
