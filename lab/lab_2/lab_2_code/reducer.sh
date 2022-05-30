#!/bin/bash
# Reads pairs from the standard input. Each tab-separated pair is composed of a studentID and a list of grades
# Returns the max grade for each student on the standard output.
# Usage:
#    STDIN: StudentID\tGrade1, StudentID\tGrade2, ...
# Output:
#    StudentID MaxGrade

python reducer.py
