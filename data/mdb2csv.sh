#!/bin/bash
FILE_NAME=$1
TABLE_NAME=$(mdb-tables $FILE_NAME)
echo $TABLE_NAME
mdb-export $FILE_NAME $TABLE_NAME > "$TABLE_NAME.csv"