from pyspark.sql import SparkSession


def create_spark_session():
    spark = SparkSession.builder \
        .appName("sparkApp") \
        .getOrCreate()
    return spark


def main():
    # creating spark session
    spark = create_spark_session()

    # create dataframe
    data = [
        ['John', 25],
        ['Smith', 30],
        ['Sarah', 28]
    ]
    rdd = spark.sparkContext.parallelize(data)
    df = spark.createDataFrame(rdd, schema='name STRING, age INT')
    df.show(5)

    # stop spark session
    spark.stop()


if __name__ == "__main__":
    main()