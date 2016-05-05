#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 4
# Taras Sotnikov

import sys
import re

# R  - 1, RD - 2, D  - 3, LD - 4, L  - 5
# K - K, P - P, else - 0
reg_exp = ['54321(?!P)',
			'(?<!54)321(?!P)',
			'132(?!P)',
			'(?<!12)345(?!K)',
			'12345(?!K)']

n_cases = int(sys.stdin.readline())
for i in range(n_cases):
	line = sys.stdin.readline().strip()
	line = line.replace("RD", "2")
	line = line.replace("LD", "4")
	line = line.replace("RU", "0")
	line = line.replace("LU", "0")
	line = line.replace("U", "0")
	line = line.replace("R", "1")
	line = line.replace("D", "3")
	line = line.replace("L", "5")
	line = line.replace("-", "")

	matches = 0
	for j in range(len(reg_exp)):
		result = re.findall(reg_exp[j], line)
		matches += len(result)

	print "Case #%d: %d" % (i+1, matches)