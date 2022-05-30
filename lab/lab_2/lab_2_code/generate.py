import os
import random
import names

DATA_NUMBER = 1000
ENTRY_NUMBER = 10000

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

    with open(os.path.join(BASE_DIR, 'id.txt'), 'w') as f:
        for i in id:
            f.write(str(i) + '\n')

    with open(os.path.join(BASE_DIR, 'firstnames.txt'), 'w') as f:
        for i in firstnames:
            f.write(i + '\n')

    with open(os.path.join(BASE_DIR, 'lastnames.txt'), 'w') as f:
        for i in lastnames:
            f.write(i + '\n')


def generate_csv():
    first = list(firstnames)
    last = list(lastnames)
    ID = list(id)
    with open("grades.csv", 'w') as f:
        for i in range(ENTRY_NUMBER):
            rand = random.randint(0, min(len(first), len(last), len(ID))-1)
            grade = random.randint(0, 100)
            f.write("{} {},{},{}\n".format(
                first[rand], last[rand], ID[rand], grade))


if "__main__" == __name__:
    generate_raw()
    generate_csv()
