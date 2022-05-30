#!/usr/bin/awk -f
# Reads grades.csv with name, studentID and grades
# Returns the tab-separated pair: studentID<TAB>grade
# Input:
#    grades.csv: hadoop,0123456789,100
# Output:
#    STDOUT: 0123456789<TAB>100

awk -F "," '{printf "%s\t%s\n", $2, $3}'
