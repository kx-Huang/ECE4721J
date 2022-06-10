from pyspark import sql
from pyspark import SparkConf, SparkContext


def get_rdd_hdfs():
    spark = sql.session.SparkSession.builder.master("yarn").appName("ex3").getOrCreate()
    return spark.read.text("hdfs://hadoop-master:8020/user/root/input/lab2/grades_1000.csv").rdd

def get_rdd_local():
    conf = SparkConf().setMaster("yarn").setAppName("ex3")
    sc = SparkContext(conf=conf).getOrCreate()

    with open("data/grades_100.csv", "r") as f:
        data = f.read().splitlines()

    return sc.parallelize(data)

def mapReduce(rdd):
    # map
    pairs = rdd.flatMap(lambda r: [r.split(",")[1:3]])

    # reduce
    max_grade = pairs.reduceByKey(lambda x, y: max([x, y]))

    for entry in max_grade.collect():
        print("{}\t{}".format(entry[0], entry[1]))


if __name__ == '__main__':
    # rdd = get_rdd_local()
    rdd = get_rdd_hdfs()
    mapReduce(rdd)
