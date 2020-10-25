''' BEGINJOBDEF
{
	"Args": {
		"--conf": "spark.yarn.executor.memoryOverhead=7g",
		"--WRITE_MODE": "append"
	},
	"DPU": 5
}
ENDJOBDEF '''


import sys
import boto3
import time
import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import functions as F, SQLContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())
#sc = SparkContext()
sqlcontext = SQLContext(glueContext.spark_session)

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'WRITE_MODE'])
db="test_virgil"
table_name="stage_vehicle"
   

df = glueContext.create_dynamic_frame.from_catalog(
             database=db,
             table_name=table_name)
df = df.toDF()

sqlcontext.registerDataFrameAsTable(df, 'stage_vehicle')

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

df = sqlcontext.sql(sql)

df = df.withColumn('job_dtm', F.lit(datetime.datetime.fromtimestamp(int(round(time.time())))))
df = df.withColumn('job_id', F.lit(args['JOB_ID']))
print ("Count: ", df.count())
df.printSchema()
df.show(5)

df.write.mode(args['WRITE_MODE']).format('parquet').save('s3://cdsatemp/virgil/core')

print('Job completed successfully')

