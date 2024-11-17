from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").geetOrCreate()

text = "Hello Spark Hello Python Airflow Hello Docker and Hello Supakorn"

words = spark.sparkContext.parallelize(text.split(" "))

workCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for wc in workCounts.collect():
    print(wc[0], wc[1])

spark.stop()