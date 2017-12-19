import scala.io.Source

object Application {

  def readLines() = {
    Source.fromFile("1.input").getLines()
  }

  def main(args: Array[String]): Unit = {
    val line = readLines().next

    val z = (line zip line.tail) :+ (line.head, line.last)
    val zf = z filter (v => v._1 == v._2) map (_._1.asDigit)
    val result1 = zf.reduce(_ + _)

    println(result1)


    val zf2 = for { i <- 0 until line.length if line(i) == line((i + line.length / 2) % line.length) } yield line(i).asDigit
    val result2 = zf2.reduce(_ + _)

    // var result2 = 0
    // for (i <- 0 until line.length) {
    //     if (line(i) == line((i + line.length / 2) % line.length)) {
    //         result2 += line(i).asDigit
    //     }
    // }
    println(result2)
  }
}
