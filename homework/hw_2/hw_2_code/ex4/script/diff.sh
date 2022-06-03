#!/bin/bash
csv_number=10

for((i=0;i<${csv_number};i++));
do
    diff data/small_generated/grades_${i}.csv data/small_extracted/grades_${i}.csv
done