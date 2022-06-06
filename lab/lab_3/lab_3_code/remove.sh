#!/bin/bash
# remove the first line (header) of the TSV files

sed -i '' '1d' name.basics.tsv
sed -i '' '1d' title.basics.tsv
sed -i '' '1d' title.principals.tsv
sed -i '' '1d' title.ratings.tsv
