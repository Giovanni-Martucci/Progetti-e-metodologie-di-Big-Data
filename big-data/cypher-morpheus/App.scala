package edu.unict.BigData

import org.apache.spark.{SparkConf,SparkContext}
import scala.math.random
import org.apache.spark.SparkContext._
import org.apache.spark.sql.{SparkSession, DataFrame}
import org.opencypher.morpheus.api.MorpheusSession
import org.opencypher.okapi.api.io.conversion.{NodeMappingBuilder, RelationshipMappingBuilder}
import org.opencypher.okapi.api.value.CypherValue
import org.opencypher.morpheus.api.io.{MorpheusNodeTable, MorpheusRelationshipTable, MorpheusElementTable}


object App {
    def main(args: Array[String]): Unit = {
      val spark = SparkSession
                   .builder()
                   .appName( name = "meyloma")
                   .config("spark.master","local[*]")
                   .getOrCreate()
     
      implicit val morpheus: MorpheusSession = MorpheusSession.local()
      import spark.sqlContext.implicits._

      val csvOptions = Map("header"->"true", "delimiter" -> ";", "inferSchema" -> "true")

      val nodesDF = spark.read.options(csvOptions).csv("nodes_elab.csv")
      val edgesDF = spark.read.options(csvOptions).csv("edges_elab.csv")

      val NodeMapping = NodeMappingBuilder.withSourceIdKey("id:ID").withImpliedLabel("Node").withPropertyKey("names", "names").withPropertyKey("size", "size").withPropertyKey("labels", "labels").withPropertyKey("rho", "rho").build
      val RelationMapping = RelationshipMappingBuilder.withSourceIdKey("identific").withSourceStartNodeKey("src:START_ID").withSourceEndNodeKey("dst:END_ID").withRelType("type").withPropertyKey("labels", "labels").withPropertyKey("mrho", "mrho").withPropertyKey("tf_idf", "tf_idf").build
      val Node = MorpheusElementTable.create(NodeMapping, nodesDF)
      val Relation = MorpheusElementTable.create(RelationMapping, edgesDF)

      val Graph = morpheus.readFrom(Node, Relation)

      val results = Graph.cypher("MATCH (dis:disease {names:'multiple myeloma'})-[r:BIO_VALUE_HIGH]->(drg:drug) RETURN dis, r, drg LIMIT 10;")
      results.show

      spark.stop()
     }
}