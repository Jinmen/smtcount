#!/bin/sh

python fetch_tweets.py
python extract_texts.py > tweets.txt
sh count.sh > result.csv
sort -t ',' -n -k 2 -r result.csv

