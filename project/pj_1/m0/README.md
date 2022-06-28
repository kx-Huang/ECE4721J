# Project 1 Milestone 0: Compact and Extract

1. Compact small `hdf5` Avro files into larger ones
2. Read `hdf5` Avro files and extract the information

## 0. Environment
- `Python`: 3.9.2
- Install `PyGreSQL` env: `$ sudo apt install libpq-dev`
- Install `python` packages: `$ python3 -m pip install -r requirements.txt`
- Remark: some syntax are modified to accommodate `Python3`

## 1. Compact small `hdf5` Avro files into larger ones

Creates an aggregate file from all song file (h5 files) in a given directory

- Usage: `$ python3 create_aggregate_file.py <H5 DIR> <OUTPUT.h5>`
- Example: `$ python3 src/create_aggregate_file.py ../MillionSongSubset/A/A/A/ data/compact.h5`
- Remark: Remove the existing file having the same name as the output file before running the python script

## 2. Read `hdf5` Avro files and extract the information

Quickly display all we know about a song/aggregate/summary file in `hdf5` format

- Usage: `$ python3 display_song.py [FLAGS] <HDF5 file> <OPT: song idx> <OPT: getter>`
- Example: `$ python3 src/display_song.py data/compact.h5 5 artist_name`
- Remark: We can find the field list of a song [here](http://millionsongdataset.com/pages/field-list/), or refer to the APIs in `hdf5_getters.py`

## 3. Run with shell scipt

```bash
chmod +x compact.sh
./compact.sh
```

## Reference
1. [MSongsDB](https://github.com/tbertinmahieux/MSongsDB)
