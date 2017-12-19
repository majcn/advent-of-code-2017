import scala.io.Source

object Application {

  def readLines() = {
    Source.fromFile("2.input").getLines()
  }

  def main(args: Array[String]): Unit = {
    val data = (readLines() map { _.split('\t') map { _.toInt }}).toList

    println {
        (data map { l => l.max - l.min }).sum
    }

    val r = data map { l =>
        val pairs = for { (x, idx) <- l.zipWithIndex; (y, idy) <- l.zipWithIndex; if idx != idy } yield (x, y)
        (pairs filter { case (a, b) => a % b == 0 } map { case (a, b) => a / b } take(1)).head
    }
    println(r.sum)
  }
}
