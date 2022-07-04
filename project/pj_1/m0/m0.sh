#!/bin/bash

mkdir -p data/
rm -f data/compact.h5

# compact hdf5 files to an aggregated file
python3 src/create_aggregate_file.py MillionSongSubset/A/A/A/ data/compact.h5

# convert hdf5 file to Avro file
python3 src/hdf5_to_avro.py -s schema/songs.avsc -i data/compact.h5 -o data/output.avro
