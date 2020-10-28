

DROP TABLE IF EXISTS myvehicle.stage_vehicle;

CREATE EXTERNAL TABLE IF NOT EXISTS myvehicle.stage_vehicle
(
	vehicle_id	STRING,
    function_id	STRING,
    entry_type	STRING,
    function_time	DOUBLE,
	job_dtm timestamp,
	job_id STRING
)
PARTITIONED BY (record_day DATE)
STORED AS PARQUET
LOCATION "s3://[[bucket]]/stage"
TBLPROPERTIES ("classification"="parquet");
MSCK REPAIR TABLE myvehicle.stage_vehicle;
