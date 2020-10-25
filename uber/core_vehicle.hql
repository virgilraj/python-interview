

DROP TABLE IF EXISTS test_virgil.core_vehicle;

CREATE EXTERNAL TABLE IF NOT EXISTS test_virgil.core_vehicle
(
	vehicle_id	STRING,
    function_id	STRING,
    start_time	DOUBLE,
	end_time 	DOUBLE,
	job_dtm timestamp,
	job_id STRING
)
STORED AS PARQUET
LOCATION "s3://cdsatemp/virgil/core"
TBLPROPERTIES ("classification"="parquet");
