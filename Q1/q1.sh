#!/bin/sh

wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz

gzip -d NASA_access_log_Aug95.gz

wc -l NASA_access_log_Aug95

egrep '18/Aug|19/Aug|20/Aug' NASA_access_log_Aug95 | cut -d '' -f 1 | sort | uniq -c | sort -r | head -10

