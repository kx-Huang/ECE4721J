#!/bin/bash
# Reads pairs from the standard input. Each tab-separated pair is composed of a studentID and a list of grades
# Returns the max grade for each student on the standard output.
# Usage:
#    STDIN: StudentID\tGrade1 Grade2 Grade3
#    e.g.: 1234567890   238 473856 5636326 56583 -349 3503 0 -349
# Output:
#    A single number as the max grade
#    e.g.:  5636326

IFS=$'\n'

while read line
do
    arr=($( echo "$line" | sed 's/.*\t//' ))
    echo "${arr[*]}" | sort -nr | head -1
done

unset IFS
