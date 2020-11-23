import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import sys

spark = SparkSession.builder.appName("A3T2").getOrCreate()
sparkContext=spark.sparkContext

wrd = sys.argv[1]
k = sys.argv[2]
shape = spark.read.option("header",True).csv(sys.argv[3])
print(type(shape))
shape_stat = spark.read.option("header",True).csv(sys.argv[4])

print(shape_stat.rdd.getNumPartitions())

shape_stat = shape_stat.repartition(20)

print(shape_stat.rdd.getNumPartitions())
start = time.time()
joined = shape_stat.join(shape, ['key_id','word'])
joined = joined.filter(joined.word.contains(wrd))
joined = joined.filter(joined.recognized.contains("False"))
joined = joined.filter(joined.Total_Strokes < int(k))

final = joined.groupBy("countrycode").count()
final = final.orderBy("countrycode")
end = time.time()

for i in final.collect():
	print(i[0], i[1], sep=",")
	
print('Time taken = ',end-start)
