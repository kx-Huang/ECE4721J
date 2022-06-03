import os
import sys
import random
import names

DATA_NUMBER = 300
if (len(sys.argv) < 2):
    print("Usage: generate.py <number of lines>")
    exit(1)
LINE_NUMBER = int(sys.argv[1])
BASE_DIR = "data/"

id = set()
firstnames = set()
lastnames = set()


def generate_raw():

    for _ in range(DATA_NUMBER):
        id.add(random.randint(1000000000, 9999999999))

    for _ in range(DATA_NUMBER):
        firstnames.add(names.get_first_name())

    for _ in range(DATA_NUMBER):
        lastnames.add(names.get_last_name())

    if (not os.path.exists(BASE_DIR)):
        os.makedirs(BASE_DIR)


def generate_csv():
    first = list(firstnames)
    last = list(lastnames)
    ID = list(id)
    with open(os.path.join(BASE_DIR, "grades_{}.csv".format(LINE_NUMBER)), 'w') as f:
        for i in range(LINE_NUMBER):
            rand = random.randint(0, min(len(first), len(last), len(ID))-1)
            grade = random.randint(0, 100)
            f.write("{} {},{},{}\n".format(
                first[rand], last[rand], ID[rand], grade))


if "__main__" == __name__:
    generate_raw()
    generate_csv()
