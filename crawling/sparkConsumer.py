from pyspark import SparkContext, SparkConf
import pyspark
from pyspark.sql import SparkSession
from pyspark.streaming.kafak import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc, explode, split

if __name__ == '__main__':
  sc = SparkContext(appName="spark_crawl")

  scc = StreamingContext(sc,10)

  message = KafkaUitls.createDirectStream(ssc, topics=[''], kafkaParams = {"metadata.broker.list":"localhost:9092"})

  words = message.map(lambda x : x[1]).flatMap(lambda x: x.split(" "))

  wordcount = words.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)

  wordcount.pprint()

  ssc.start()
  ssc.awaitTermination()

# spark = SparkSession\
#   .builder\
#   .appName("StructuredNetworkWordCount")\
#   .getOrCreate()

# lines = spark \
#     .readStream \
#     .format("socket") \
#     .option("host", "localhost") \
#     .option("port", 9999) \
#     .load()

# words = lines.select(
#    explode(
#        split(lines.value, " ")
#    ).alias("word")
# )

# wordCounts = words.groupBy("word").count()

# query = wordCounts \
#     .writeStream \
#     .outputMode("complete") \
#     .format("console") \
#     .start()

# query.awaitTermination()