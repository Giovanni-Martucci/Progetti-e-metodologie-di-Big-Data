
package it.unict.BigData;
  
import org.apache.spark.{SparkConf,SparkContext}
import scala.math.random
import org.apache.spark.SparkContext._
import org.apache.spark.sql.{SparkSession, DataFrame}
import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

object App
{
    def main(args: Array[String]) 
    {
        //val spark = SparkSession.builder().master("local[*]").appName("Graphx").getOrCreate()
	val conf = new SparkConf().setMaster("local[*]").setAppName("Graphx")
        val sc = new SparkContext(conf)
      
	sc.setLogLevel("ERROR")
	println("spark read csv files from a directory into RDD")
	val rddNodesFile = sc.textFile("nodes_elab.csv")
    val rddEdgesFile = sc.textFile("edges_elab.csv")
	println(rddNodesFile.getClass)
    println(rddEdgesFile.getClass)
	
	val rdd_nodes = rddNodesFile.map(f=>{f.split(";")})
	val rdd_edges = rddEdgesFile.map(f=>{f.split(";")})

	val rdd_nodes_ = rdd_nodes.mapPartitionsWithIndex((index, it) => if (index == 0) it.drop(1) else it, preservesPartitioning = true)
	val rdd_edges_ = rdd_edges.mapPartitionsWithIndex((index, it) => if (index == 0) it.drop(1) else it, preservesPartitioning = true)
	

	var rdd_nodes_final: RDD[(VertexId, (String, Int, String))] = rdd_nodes_.map(node => (
                  node(0).toLong, ( node(2), node(3).toInt, node(4) )
    ))

	var rdd_edges_final: RDD[Edge[String]] = rdd_edges_.map(node => Edge(
                  node(1).toLong, node(3).toLong, ( node(5) +" "+ node(6) )
	))


	val defaultNodes = ("",0,"")

	val graph = Graph(rdd_nodes_final, rdd_edges_final, defaultNodes)

	val degrees: VertexRDD[Int] = graph.degrees
	println("\n\n")
	println(degrees.take(10))
	println("\n\n")	
	println(degrees)
	println("\n\n")	

    }
}
