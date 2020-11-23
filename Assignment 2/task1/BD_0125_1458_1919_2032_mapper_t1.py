#!/usr/bin/python3

import sys

# Get input lines from stdin
for line in sys.stdin:

	# Remove extra space
	data = line.strip()
	if data[0] == "#":
		continue
	data=data.split()
	if len(data)==2:
		# Get From and To nodes
		source, destination = data
		# Printing Source and destination
		print("%s\t%s" % (source,destination))
