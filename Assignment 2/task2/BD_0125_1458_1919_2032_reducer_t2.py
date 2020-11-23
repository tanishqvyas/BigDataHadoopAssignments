#!/usr/bin/python3

import sys

def main(separator="\t"):
	sum_cont=0
	cur_node=None
	for line in sys.stdin:
		data=line.strip()
		node,contribution=data.split(separator,1)
		try:
			contribution=float(contribution)
		except ValueError:
			continue
		if cur_node==node:
			sum_cont+=contribution
		else:
			if cur_node:
				s="{0:.5f}".format(((0.85*sum_cont)+0.15))
				print(cur_node+", "+str(s))
			cur_node=node
			sum_cont=contribution
	if cur_node==node:
		s="{0:.5f}".format(((0.85*sum_cont)+0.15))
		print(cur_node+", "+str(s))

if __name__ == '__main__':
	main()
