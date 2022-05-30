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
