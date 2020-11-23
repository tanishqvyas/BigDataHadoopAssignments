#!/usr/bin/python3

import sys


def main(separator="\t"):
	adj_list=[]
	cur_source=None
	f=open(sys.argv[1],"a")
	for line in sys.stdin:
		data = line.strip()

		# Get From and To nodes
		source, destination = data.split(separator,1)
		# Check If node is already present in the graph
		if cur_source==source:
			# Variable to keep track of insertion
			isInserted = False

			# Iterating through neighbours to find a place to insert
			for i in range(len(adj_list)):
				if(adj_list[i] < destination):
					continue
				else:
					adj_list.insert(i, destination)
					isInserted = True
					break
			# Insertion at the end if the new node is largest lexicographically
			if(not isInserted):
				adj_list.append(destination)
		else:
			if cur_source:
				f.write(cur_source+", "+str(1))
				f.write("\n")
				print(cur_source, end=separator)
				print("[", end="")
				
				length = len(adj_list)

				for node in range(length):

					if(node == length-1):
						print(adj_list[node], end="")

					else:
						print(adj_list[node], ",", sep="", end=" ")

				print("]")
			cur_source=source
			adj_list=[destination]
	if cur_source==source:
		f.write(cur_source+", "+str(1))
		f.write("\n")
		print(cur_source, end=separator)
		print("[", end="")
		
		length = len(adj_list)

		for node in range(length):

			if(node == length-1):
				print(adj_list[node], end="")

			else:
				print(adj_list[node], ",", sep="", end=" ")

		print("]")
	f.close()

if __name__ == '__main__':
	main()
