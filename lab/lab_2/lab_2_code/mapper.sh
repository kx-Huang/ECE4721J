#!/bin/bash
# Reads STDIN with name, studentID and grades separated by newline
# Returns the tab-separated pair: studentID<TAB>grade
# Input:
#    STDIN: Michael Huang,0123456789,100
# Output:
#    STDOUT: 0123456789<TAB>100

awk -F, '{print $2"\t"$3}'
