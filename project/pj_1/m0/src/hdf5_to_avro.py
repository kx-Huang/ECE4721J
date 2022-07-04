import os
import time
import argparse
from tqdm import tqdm

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

import hdf5_getters


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def info():
    return f"{bcolors.OKCYAN}[Info]{bcolors.ENDC}"


def error():
    return f"{bcolors.FAIL}[Error]{bcolors.ENDC}"


def warning():
    return f"{bcolors.WARNING}[Warn]{bcolors.ENDC}"


def red(string):
    return f"{bcolors.FAIL}%s{bcolors.ENDC}" % string


def blue(string):
    return f"{bcolors.OKCYAN}%s{bcolors.ENDC}" % string


def orange(string):
    return f"{bcolors.WARNING}%s{bcolors.ENDC}" % string


def get_time():
    return time.strftime(f"{bcolors.HEADER}%H:%M:%S{bcolors.ENDC}", time.localtime())


def parser():

    # command line parser
    parser = argparse.ArgumentParser(
        description='Convert a song file from hdf5 to Avro')

    parser.add_argument(
        "-s", "--schema", help="Avro schema file", dest="schema", required=True)
    parser.add_argument(
        "-i", "--input", help="hdf5 input file", dest="hdf5", required=True)
    parser.add_argument(
        "-o", "--output", help="Avro output file", dest="avro", required=True)

    args = parser.parse_args()

    if args.schema and args.hdf5 and args.avro:
        print(get_time(), info(), "Convert a song file from hdf5 to Avro...")
        print(get_time(), info(), "Avro schema path:", blue(args.schema))
        print(get_time(), info(), "hdf5 input path:", blue(args.hdf5))
        print(get_time(), info(), "Avro output path:", blue(args.avro))

    # check if input files exist
    if os.path.exists(args.schema) and os.path.exists(args.hdf5):
        print(get_time(), info(), "Avro schema file and hdf5 file exist")
    else:
        print(get_time(), error(), "Avro schema file or hdf5 file don't exist")

    # check if output file exist
    if os.path.exists(args.avro):
        print(get_time(), warning(),
              "Avro output file {} already exists".format(orange(args.avro)))

    return [args.schema, args.hdf5, args.avro]


def get_field_type(field):
    if "string" in field:
        return str
    if "int" in field:
        return int
    if "float" in field:
        return float
    return None


def hdf5_to_avro(files):
    # get file path
    path_schema = files[0]
    path_hdf5 = files[1]
    path_avro = files[2]

    # parse avro schema
    print(get_time(), info(), "Parsing the Avro schema file...")
    schema = avro.schema.parse(open(path_schema, "rb").read())

    # check all fields in schema
    fields = schema.__dict__["_props"]["fields"]
    for field in fields:
        my_getter = 'get_' + field.name
        if not hasattr(hdf5_getters, my_getter):
            print(get_time(), error(), 'getter requested:',
                  red(my_getter), 'does not exist. Please change the field name according to', blue('hdf5_getters'))

    # add the fields to song info dict for convertion
    print(get_time(), info(), "Get the following fields:")
    for field in fields:
        print("\t\t{:<28s} {:<20s}".format(blue(field.name), str(field.type)))

    # retrieve song infromation from hdf5 file with hdf5_getters.py
    hdf5 = hdf5_getters.open_h5_file_read(path_hdf5)

    # get song number
    num_song = hdf5_getters.get_num_songs(hdf5)
    print(get_time(), info(), "Found", blue(num_song), "song(s)")

    # get song(s) information and write to avro file
    song_info = {}
    writer = DataFileWriter(open(path_avro, "wb"), DatumWriter(), schema)
    print(get_time(), info(), "Start converting {} to {}".format(
        blue("hdf5"), blue("Avro")))
    for i in tqdm(range(num_song), desc=get_time()+blue(" Converting")):
        for field in fields:
            res = hdf5_getters.__getattribute__(
                "get_{}".format(field.name))(hdf5, i)
            # type check
            type = get_field_type(field.__str__())
            if type is str:
                song_info[field.name] = str(res)
            elif type is float:
                song_info[field.name] = float(res)
            elif type is int:
                song_info[field.name] = int(res)
            else:
                song_info[field.name] = res
        writer.append(song_info)
    writer.close()

    # for validation and debug
    # reader = DataFileReader(open(path_avro, "rb"), DatumReader())
    # for song in reader:
    #     print(song)
    # reader.close()


if __name__ == "__main__":
    hdf5_to_avro(parser())
