import random

def generate():

    LENGTH = 20

    NAME = ["Michael", "Girotti", "Aranda", "Maharaj", "Prien", "Farnleitner", "Page", "Moeyens", "Chambers", "Boese", "Antonik", "Anthony", "Andrew", "Cindy", "Alice", "Bruce", "Tom"]

    FIRSTNAME = ["Huang", "Zhang", "Yang", "Wu", "Shi", "Liu", "Wang", "Zhao", "Hu", "Lu", "Gong", "Xue"]

    MAILBOX = ["gmail.com", "sjtu.edu.cn", "umich.edu", "foxmail.com", "hotmail.com", "outlook.com"]

    with open('roster.csv', 'w') as f:
        for _ in range(LENGTH):

            name = NAME[random.randint(0, len(NAME)-1)]
            firstname = FIRSTNAME[random.randint(0, len(FIRSTNAME)-1)]
            mailbox = MAILBOX[random.randint(0, len(MAILBOX)-1)]

            f.write('{},{},{}.{}@{}\n'.format(name, firstname, name.lower(), firstname.lower()[0], mailbox))

if __name__ == '__main__':
    generate()
