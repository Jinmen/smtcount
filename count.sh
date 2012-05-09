#!/bin/sh

while read title; do
  echo -n "${title},"
  grep -i "${title}" tweets.txt | wc -l
done < setlist.txt
