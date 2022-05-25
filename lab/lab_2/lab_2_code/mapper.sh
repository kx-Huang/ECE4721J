#!/bin/bash
# Reads grades.csv with name, studentID and grades
# Returns the tab-separated pair: studentID<TAB>grade
# Input:
#    grades.csv: hadoop,0123456789,100
# Output:
#    STDOUT: 0123456789<TAB>100

INPUT='grades.csv'
IFS=$','

[ ! -f $INPUT ] && { echo "ERROR: $INPUT file not found"; exit -1; }
while read name id grade
do
    echo -e "$id\t$grade"
done < $INPUT

unset IFS
