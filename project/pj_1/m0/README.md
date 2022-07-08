# Project 1 Milestone 0: HDF5 Data Pre-process

1. Compact small `hdf5` files into larger one
2. Read `hdf5` file and extract the information
3. Convert `hdf5` to `Avro` with `Apache Avro™`

## 0. Environment
- `Python`: 3.9.2
- Install `PyGreSQL` env: `$ sudo apt-get install libpq-dev`
- Install `python` packages: `$ python3 -m pip install -r requirements.txt`
- Remark: some syntax are modified to accommodate `Python 3`

## 1. Compact small `hdf5` files into larger one

Creates an aggregate file from all song `hdf5` files in a given directory

- Usage: `$ python3 create_aggregate_file.py <H5 DIR> <OUTPUT.h5>`
- Input: a directory contains `hdf5` song files
- Output: an aggregate `hdf5` song file
- Example: `$ python3 src/create_aggregate_file.py data/single/ data/compact.h5`
- Remark: Remove the existing file having the same name as the output file before running the `Python` script

## 2. Read `hdf5` files and extract the information

Quickly display all we know about a single/aggregate/summary `hdf5` song file

- Usage: `$ python3 display_song.py [FLAGS] <HDF5 file> <OPT: song idx> <OPT: getter>`
- Input: a `hdf5` song file
- Output: specified field content
- Example: `$ python3 src/display_song.py data/compact.h5 5 artist_name`
- Remark: We can find the field list of a song [here](http://millionsongdataset.com/pages/field-list/), or refer to the APIs in `hdf5_getters.py`

## 3. Convert `hdf5` to `Avro` with `Apache Avro™`

Convert a single/aggregate song file from `hdf5` to `Avro`

- Usage: `$ hdf5_to_avro.py [-h] -s <SCHEMA> -i <HDF5> -o <AVRO>`
- Input: an `Avro` schema file, a `hdf5` song file to be converted
- Output: an `Avro` song file
- Example: `$ python3 src/hdf5_to_avro.py -s schema/songs.avsc -i data/compact.h5 -o data/output.avro`
- Remark: field names in schema file must correspond to getters in `hdf5_getters.py`. A sanity check will be performed before conversion

## 4. Run all process with shell script

- Usage:
  ```bash
  $ chmod +x m0.sh
  $ ./m0.sh
  ```

## Reference

1. [MSongsDB](https://github.com/tbertinmahieux/MSongsDB)
2. [MSongsDB Field List](http://millionsongdataset.com/pages/field-list/)
3. [Apache Avro™ Documentation](https://avro.apache.org/docs/current/index.html)
