from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
import sys

spark = SparkSession.builder.appName("A3T1").getOrCreate()

df = spark.read.option("header",True).csv(sys.argv[3])
wrd = sys.argv[1]

df1 = df.filter(df.word.contains(wrd))

df2_t = df1.filter(df1.recognized.contains("True"))
df2_f = df1.filter(df1.recognized.contains("False"))

avg_t = df2_t.select(avg("Total_Strokes")).collect()[0][0]
avg_f = df2_f.select(avg("Total_Strokes")).collect()[0][0]


if(avg_t == None):
	avg_t = 0
if(avg_f == None):
	avg_f = 0

print("{0:.5f}".format(avg_t))
print("{0:.5f}".format(avg_f))

spark.stop()