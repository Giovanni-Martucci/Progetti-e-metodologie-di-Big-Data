import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD


val spark:SparkSession = SparkSession.builder()
    .master("local[*]")
    .appName("Graphx")
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

println("spark read csv files from a directory into RDD")
val rddNodesFile = spark.sparkContext.textFile("nodes_elab.csv")
val rddEdgesFile = spark.sparkContext.textFile("edges_elab.csv")
println(rddFromFile.getClass)

val rdd_nodes = rddNodesFile.map(f=>{f.split(",")})
val rdd_edges = rddEdgesFile.map(f=>{f.split(",")})


val graph = Graph(rdd_nodes, rdd_edges)

val Degrees: VertexRDD[Int] = graph.degrees

def max(a: (VertexId, Int), b: (VertexId, Int)): (VertexId, Int) = {
  if (a._2 > b._2) a else b
}

val maxDegrees: (VertexId, Int)   = graph.degrees.reduce(max)


