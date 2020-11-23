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
				c=round((0.15+(0.85*sum_cont)),5)
				s="{0:.5f}".format(c)
				print(cur_node+", "+str(s))
			cur_node=node
			sum_cont=contribution
	if cur_node==node:
		c=round((0.15+(0.85*sum_cont)),5)
		s="{0:.5f}".format(c)
		print(cur_node+", "+str(s))

if __name__ == '__main__':
	main()
