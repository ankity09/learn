-- Pig Example --

--Script to find the max Temp recorded by year for the weather dataset from Hadoop Definitive Guide

records = LOAD 'input/path/to/file' AS (year:chararray, temperature:int, quality:int);

/*
The above statement creates a realtion called "record" and loads the data spcified by the path.The relation has a schema given by the "AS" keyword followed by the Scehma itself. The year:chararray notation describes the filed's name and type and so on. The result of the LOAD operator is a relation, which os just a set of tuples. A tuple is like a row of data in a database table.
*/

filtered_records = FILTER records BY temperature != 9999 AND quality IN (0,1,4,5,9);

/*
The above statement removes records that have a missing temparture (indicated by 9999) or an unstaisfactory quality reading 
*/

grouped_records = GROUP filtered_records BY year;

/*
*/

max_temp = FOREACH grouped_records GENERATE group, MAX(filtered_records.temperature);

/*
*/

DUMP max_temp;
