from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]")\
    .appName("Generate test files {}".format(__file__)).getOrCreate()

spark.read.parquet("/home/bartosz/workspace/wfc-playground/feature-store-feast/output_features").show(truncate=False)
