#!/bin/bash
# Reads STDIN with name, studentID and grades separated by newline
# Returns the tab-separated pair: studentID<TAB>grade
# Input:
#    STDIN: hadoop,0123456789,100
# Output:
#    STDOUT: 0123456789<TAB>100

awk -F "," '{printf "%s\t%s\n", $2, $3}'
