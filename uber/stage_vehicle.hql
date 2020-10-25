

DROP TABLE IF EXISTS test_virgil.stage_vehicle;

CREATE EXTERNAL TABLE IF NOT EXISTS test_virgil.stage_vehicle
(
	vehicle_id	STRING,
    function_id	STRING,
    entry_type	STRING,
    function_time	DOUBLE,
	job_dtm timestamp,
	job_id STRING
)
STORED AS PARQUET
LOCATION "s3://cdsatemp/virgil/stage"
TBLPROPERTIES ("classification"="parquet");

