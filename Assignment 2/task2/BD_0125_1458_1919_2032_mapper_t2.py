#!/usr/bin/python3

import sys
f=open(sys.argv[1],"r")
pageranks=dict()
for i in f.readlines():
	key,value=i.strip().split(",",1)
	pageranks[key]=float(value.strip())
f.close()
for line in sys.stdin:
	data = (line.strip()).split("\t",1)
	# Get From and To nodes
	source, destination = data
	destination=destination.strip('][').split(',')
	print(source,0,sep="\t") # will handle the case for ones having no incoming links eventually
	try:
		contribution=(pageranks[source]/len(destination))		# this will throw KeyError if source not in pageranks
		# Printing each node linked to from source and contribution of source node
		for d in destination:
			d=d.strip()
			try:
				check=pageranks[d]					#this might throw exception
				print(d,contribution,sep="\t")
			except KeyError:
				continue
	except KeyError:
		continue
