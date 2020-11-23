from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import sys

spark = SparkSession.builder.appName("A3T1").getOrCreate()

# Retrive word and the value of K
wrd = sys.argv[1]
k = int(sys.argv[2])

# Reading the two csv files
shape = spark.read.option("header",True).csv(sys.argv[3])
shape_stat = spark.read.option("header",True).csv(sys.argv[4])


# Joining the Dataframes
joined = shape_stat.join(shape, ['key_id','word'])



# Filters

# Check presence of word
joined = joined.filter(joined.word.contains(wrd))

# Check recog status = False
joined = joined.filter(joined.recognized.contains("False"))

# Check num strokes < K
joined = joined.filter(joined.Total_Strokes < k)


# Grouping Entries by country and sorting them
final = joined.groupBy("countrycode").count()
final = final.orderBy("countrycode")



if(len(final.collect()) > 0):
	for i in final.collect():
		print(i[0], i[1], sep=",")
else:
	print("0")