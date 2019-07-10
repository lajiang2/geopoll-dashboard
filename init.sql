CREATE TABLE geopoll (
	date VARCHAR(255),
	day VARCHAR(255),
	time_block VARCHAR(255),
	sample_size INT,
	station VARCHAR(255),
	viewers INT,
	tv_show VARCHAR(255),
	language VARCHAR(255),
	country VARCHAR(255),
	PRIMARY KEY (date, time_block, station, country)
);