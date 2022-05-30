import random
import names

NUMBER = 1000

id = set()
firstnames = set()
lastnames = set()

for _ in range(NUMBER):
    id.add(random.randint(1000000000, 9999999999))

for _ in range(NUMBER):
    firstnames.add(names.get_first_name())

for _ in range(NUMBER):
    lastnames.add(names.get_last_name())


with open('id.txt', 'w') as f:
    for i in id:
        f.write(str(i) + '\n')

with open('firstnames.txt', 'w') as f:
    for i in firstnames:
        f.write(i + '\n')

with open('lastnames.txt', 'w') as f:
    for i in lastnames:
        f.write(i + '\n')
