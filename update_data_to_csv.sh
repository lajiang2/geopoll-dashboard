#!/bin/bash
pushd "./data/update" > /dev/null
for FILENAME in *.xlsx; do
	FILENAMELEN=${#FILENAME}
	CSVNAME=${FILENAME:0:FILENAMELEN-5}.csv
	in2csv $FILENAME > $CSVNAME
done
