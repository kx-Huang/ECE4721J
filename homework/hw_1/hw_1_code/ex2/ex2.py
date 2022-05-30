import bz2
import os
from re import X
import sys
import zipfile
import pandas as pd
from sklearn import linear_model
from tqdm import tqdm


BASE_DIR = '/Users/michaelhuang/Desktop/ECE4721J/homework/hw_1/hw_1_code/ex2/'
DATA_DIR = BASE_DIR + 'flight_data/'


# unzip all files
def unzip_file(_file, _destination):
    with zipfile.ZipFile(_file, 'r') as zip_file:
        zip_file.extractall(_destination)


# get flight entry as a dictionary
def get_flight_entry(col_names, row):
    entry = {}
    row_contents = row.split(',')
    for i, col_name in enumerate(col_names):
        try:
            entry[col_name] = int(row_contents[i])
        except ValueError:
            entry[col_name] = row_contents[i]
        except IndexError:
            # end of file or something unexpected
            return None
    return entry


def get_statistics():
    carriers_delay_count = {}
    origins_late_count = {}
    carriers_longest_delay = {}

    for file_bz2 in os.listdir(DATA_DIR):

        if file_bz2.startswith('._') or not file_bz2.endswith('.bz2'):
            continue

        print('Processing {}...'.format(file_bz2), file=sys.stderr)
        with bz2.open(os.path.join(DATA_DIR, file_bz2)) as f:

            # get rows as a list
            rows = str(f.read()).split('\\n')
            # get column names which is the first row
            col_names = rows[0].split(',')

            # process each file and generate process bar
            for row in tqdm(rows[1:]):
                flight = get_flight_entry(col_names, row)
                if flight is not None:
                    # delay count
                    try:
                        flight_count = carriers_delay_count.get(flight['UniqueCarrier'], 0)
                        if type(flight['DepDelay']) == int and flight['DepDelay'] > 0:
                            flight_count += 1
                        carriers_delay_count[flight['UniqueCarrier']] = flight_count
                    except TypeError:
                        ...
                    # late origin count
                    try:
                        origin_count = origins_late_count.get(flight['Origin'], 0)
                        if type(flight['WeatherDelay']) == int and flight['WeatherDelay'] > 0:
                            origin_count += 1
                        origins_late_count[flight['Origin']] = origin_count
                    except TypeError:
                        ...
                    # longest delay
                    try:
                        flight_longest_delay = carriers_longest_delay.get(flight['UniqueCarrier'], 0)
                        if type(flight['DepDelay']) == int and flight['DepDelay'] > flight_longest_delay:
                            carriers_longest_delay[flight['UniqueCarrier']] = flight['DepDelay']
                    except TypeError:
                        ...

    print('----- 2.a -----')
    name = max(carriers_delay_count, key=carriers_delay_count.get)
    print("Most commonly late carrier: {}".format(name))
    print("Late count: {} times".format(carriers_delay_count[name]))

    print('----- 2.b -----')
    print("3 most commonly late origins due to bad weather:")
    top_3 = sorted(origins_late_count, key=origins_late_count.get, reverse=True)[:3]
    for name in top_3:
        print("{} delays {} times".format(name, origins_late_count[name]))

    print('----- 2.c -----')
    print("Longest delay experienced for each carrier")
    for name, time in carriers_longest_delay.items():
        print("{}: {}".format(name, time))

def get_pattern_2008():
    # get data from 2008
    df = pd.read_csv(os.path.join(DATA_DIR, "2008.csv.bz2"))

    # drop rows with missing values
    data = df[['DayOfWeek', 'DepTime', 'CRSDepTime', 'ArrTime', 'CRSArrTime', 'DepDelay']]
    data = data.dropna()

    # get features and target
    X = data[['DayOfWeek', 'DepTime', 'CRSDepTime', 'ArrTime', 'CRSArrTime']]
    Y = data['DepDelay']

    # fit linear regression model
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)

    print(regr.coef_)


if __name__ == '__main__':
    unzip_file('flights.zip', BASE_DIR)
    get_statistics()
    get_pattern_2008()
