import pyspark
import batchutil
import pandas as pd
import os
import uuid
import time
import datetime
from pyspark import SparkContext
from pyspark.sql import functions as F, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType
from pyspark.sql.functions import array, lit

#findspark.init()
#os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"

SPLIT_COUNT = 100000

# Create Spark session
sc = SparkSession.builder.appName("CokeBatch")\
    .config ("spark.sql.shuffle.partitions", "50")\
    .config("spark.driver.maxResultSize","50g")\
    .config ("spark.sql.execution.arrow.pyspark.enabled", "true")\
    .config("spark.sql.debug.maxToStringFields","5000") \
    .config("spark.executor.cores", "3") \
    .config("spark.executor.memory", "10g") \
    .config("spark.cores.max", "3") \
    .config("spark.logConf", "true")\
    .getOrCreate()

sqlContext = SQLContext(sc)


bkt = 'cdsatemp'

def process():
    s3path = 'virgil/stage/'
    all_files = batchutil.list_keys(bkt, s3path)
    
    for filename in all_files:
        if '.parquet' in filename:
            print(filename)
            is_saved = batchutil.save_to_temp(bkt, filename)
            print(is_saved[0])
            #    all_df.append(spark_process(is_saved[1]))
            #    batchutil.delete_from_temp(is_saved[1])
    
    spark_process()


def spark_process():
    s3path = 'virgil/core'
    job_id = str(uuid.uuid1())
    print(job_id)
    ti = datetime.datetime.fromtimestamp(int(round(time.time())))
    print('start spark ::')
    flat_df = sc.read.parquet("temp/part*.parquet")
    flat_df.printSchema()
    flat_df = flat_df.select(['vehicle_id','function_id','entry_type','function_time'])

    sqlContext.registerDataFrameAsTable(flat_df, 'stage_vehicle')

    sql = "select \
    s.vehicle_id, \
    s.function_id, \
    s.function_time as start_time, \
    e.function_time as end_time \
    from( \
    select * from \
        ( \
        select \
            vehicle_id,\
            function_id,\
            function_time, \
            ROW_NUMBER() OVER (\
            partition by vehicle_id, function_id	ORDER BY vehicle_id, function_id,function_time\
            ) rn\
            from stage_vehicle  \
        where entry_type = 'start' \
        order by 1,2,3 \
        )\
        )s join \
    (\
    select \
        vehicle_id,\
        function_id, \
        function_time,\
        ROW_NUMBER() OVER (\
        partition by vehicle_id, function_id	ORDER BY vehicle_id, function_id,function_time \
    ) rn\
    from stage_vehicle \
    where entry_type = 'end' \
    order by 1,2,3) e \
    on s.vehicle_id = e.vehicle_id \
    and s.function_id=e.function_id \
    and s.rn = e.rn"

    flat_df = sqlContext.sql(sql)
    flat_df = flat_df.withColumn("job_id", lit(job_id))
    flat_df = flat_df.withColumn('job_dtm', lit(ti))
    flat_df.show(5)
    print("count", flat_df.count())
    flat_df.write.mode('append').format('parquet').save('out/')
    batchutil.write_out_to_s3_parquet(s3path, bkt)
    batchutil.remove_out_file()

if __name__ == "__main__":
    process()
    