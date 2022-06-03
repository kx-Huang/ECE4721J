#!/usr/bin/python3
# coding:utf-8

# Reads pairs from the standard input. Each tab-separated pair is composed of a studentID and a list of grades
# Returns the max grade for each student on the standard output.
#
# Input:
#    StudentID<TAB>Grade1
#    StudentID<TAB>Grade2
#    ...
# Output:
#    StudentID Max(Grade1, Grade2, ...)


import sys


def reduce():

    roster = {}

    # build roster
    line = sys.stdin.readline()
    while line:
        entry = line.split()
        ID = entry[0]
        grade = int(entry[1])
        roster.setdefault(ID, []).append(grade)
        line = sys.stdin.readline()

    # find max grade
    for ID in sorted(roster.keys()):
        print("{} {}".format(ID, max(roster[ID])))


if "__main__" == __name__:
    reduce()
