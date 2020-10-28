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
from pyspark.sql.functions import array, lit

# Create Spark session
sc = SparkSession.builder.appName("CokeBatch")\
    .config ("spark.sql.shuffle.partitions", "50")\
    .config("spark.driver.maxResultSize","50g")\
    .config ("spark.sql.execution.arrow.pyspark.enabled", "true")\
    .config("spark.sql.debug.maxToStringFields","5000") \
    .config("spark.logConf", "true")\
    .getOrCreate()


bkt = 'my-vehicle'

def process():
    s3path = 'landing/'
    
    all_files = batchutil.list_keys(bkt, s3path)
    
    for filename in all_files:
        if '.csv' in filename:
            print(filename)
            is_saved = batchutil.save_to_temp(bkt, filename)
            print(is_saved[0])
            if(is_saved[0]):
                spark_process(is_saved[1])
                batchutil.delete_from_temp(is_saved[1])

def spark_process(file):
    s3path = 'stage/'
    job_id = str(uuid.uuid1())
    ti = datetime.datetime.fromtimestamp(int(round(time.time())))
    print('start spark ::' + file)
    flat_df = sc.read.csv(file)
    flat_df = flat_df.withColumn("job_id", lit(job_id))
    flat_df = flat_df.withColumn('job_dtm', lit(ti))
    flat_df = (flat_df.withColumnRenamed('_c0','vehicle_id')
                    .withColumnRenamed('_c1','function_id')
                    .withColumnRenamed('_c2','entry_type')
                    .withColumnRenamed('_c3','function_time')
                    )
    flat_df.show(2)
    flat_df.write.mode('append').format('parquet').save('out/')
    batchutil.write_out_to_s3_parquet(s3path, bkt)
    batchutil.remove_out_file()

if __name__ == "__main__":
    process()
    