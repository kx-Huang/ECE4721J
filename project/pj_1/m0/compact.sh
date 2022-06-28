#!/bin/bash
mkdir -p data/
rm -f data/compact.h5
python3 src/create_aggregate_file.py ../MillionSongSubset/A/A/A/ data/compact.h5
python3 src/display_song.py data/compact.h5 5 artist_name
