

DROP TABLE IF EXISTS myvehicle.landing_vehicle;

CREATE EXTERNAL TABLE IF NOT EXISTS myvehicle.landing_vehicle
(
	vehicle_id	STRING,
    function_id	STRING,
    entry_type	STRING,
    function_time	DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES(
	'separatorChar' = ',',
	'quoteChar' = '\"',
	'escapeChar' = '\''
)
STORED AS TEXTFILE
LOCATION "s3://[[bucket]]/landing"
TBLPROPERTIES ("serialization.null.format"="","classification"="csv");
