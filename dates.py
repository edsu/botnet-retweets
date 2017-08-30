#!/usr/bin/env python 

import csv
import sys

from dateutil.parser import parse

input_file = sys.argv[1]

cols = ["screen_name", "followers_count", "friends_count", "statuses_count", "created_at", "lang" ]

output = csv.DictWriter(sys.stdout, cols)
otuput.writeheader()

for row in csv.DictReader(open(input_file)):
    row['created_at'] = parse(row['created_at']).strftime("%Y-%m-%dT%H:%M:%S")
    output.writerow(row)

