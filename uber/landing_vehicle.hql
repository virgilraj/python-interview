

DROP TABLE IF EXISTS test_virgil.landing_vehicle;

CREATE EXTERNAL TABLE IF NOT EXISTS test_virgil.landing_vehicle
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
LOCATION "s3://cdsatemp/virgil/landing"
TBLPROPERTIES ("serialization.null.format"="","classification"="csv");
