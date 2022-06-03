import os
import random
import names

DATA_NUMBER = 1000
ENTRY_NUMBER = 100
CSV_NUMBER = 10

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

def generate_csv(csv_number):
    first = list(firstnames)
    last = list(lastnames)
    ID = list(id)
    csv_name = "grades_" + str(csv_number) + ".csv"
    with open(os.path.join(BASE_DIR, csv_name), 'w') as f:
        for i in range(ENTRY_NUMBER):
            rand = random.randint(0, min(len(first), len(last), len(ID))-1)
            grade = random.randint(0, 100)
            f.write("{} {},{},{}\n".format(
                first[rand], last[rand], ID[rand], grade))


if "__main__" == __name__:
    generate_raw()
    for i in range(CSV_NUMBER):
        generate_csv(i)
