#!/bin/bash
# Call grading.awk and create a csv file named grades.csv

OUTPUT=grades.csv

awk -f grading.awk > $OUTPUT
