#!/bin/sh
CONVERGE=1
rm v* log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /output* 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-mapper "/home/hadoop/BD/Assignment2/mapper1.py" \
-reducer "/home/hadoop/BD/Assignment2/reducer1.py  '/home/hadoop/BD/Assignment2/v'"  \
-input /web-Google.txt \
-output /output1 #has adjacency list


while [ "$CONVERGE" -ne 0 ]
do
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
	-mapper "/home/hadoop/BD/Assignment2/mapper2.py '/home/hadoop/BD/Assignment2/v' " \
	-reducer "/home/hadoop/BD/Assignment2/reducer2.py" \
	-input /output1 \
	-output /output2
	touch v1
	hadoop fs -cat /output2/* > /home/hadoop/BD/Assignment2/v1
	CONVERGE=$(python3 check_conv.py >&1)
	hdfs dfs -rm -r /output2
	echo $CONVERGE

done
