

DROP TABLE IF EXISTS myvehicle.core_vehicle;

CREATE EXTERNAL TABLE IF NOT EXISTS myvehicle.core_vehicle
(
	vehicle_id	STRING,
    function_id	STRING,
    start_time	DOUBLE,
	end_time 	DOUBLE,
	job_dtm timestamp,
	job_id STRING
)
PARTITIONED BY (record_day DATE)
STORED AS PARQUET
LOCATION "s3://[[bucket]]/core"
TBLPROPERTIES ("classification"="parquet");
MSCK REPAIR TABLE myvehicle.core_vehicle;
