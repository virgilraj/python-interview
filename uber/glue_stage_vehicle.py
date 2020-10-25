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
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'WRITE_MODE'])
db="test_virgil"
table_name="landing_vehicle"

def move_to_archive():
    s3 = boto3.resource('s3')
    src_bucket = s3.Bucket('cdsatemp')
    dest_bucket = s3.Bucket('cdsatemp')
    for obj in src_bucket.objects.all():
        if('virgil/landing/' in obj.key and '.csv' in obj.key):
            filename= obj.key.split('/')[-1]
            dest_bucket.put_object(Key='virgil/archive/' + filename, Body=obj.get()["Body"].read())
            #s3.Object(src_bucket, obj.key).delete()
   

df = glueContext.create_dynamic_frame.from_catalog(
             database=db,
             table_name=table_name)
df = df.toDF()
df = df.withColumn('job_dtm', F.lit(datetime.datetime.fromtimestamp(int(round(time.time())))))
df = df.withColumn('job_id', F.lit(args['JOB_ID']))
print ("Count: ", df.count())
df.printSchema()
df.show(5)

df.write.mode(args['WRITE_MODE']).format('parquet').save('s3://cdsatemp/virgil/stage')
move_to_archive()
print('Job completed successfully')

