#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 2
# Taras Sotnikov

import sys
import collections

with open('corpus.txt', 'r') as f:
	all_words = f.readline().split()

	n_cases = int(sys.stdin.readline())
	for i in range(n_cases):
		line = sys.stdin.readline().split()
		ini = int(line[0]) - 1
 		end = int(line[1])
 		words = all_words[ini:end]
 		counter = collections.Counter(words)
 		result = 'Case #%d: ' % (i +1)
 		result += ",".join('%s %d' % (aux[0],aux[1]) for aux in counter.most_common(3))
 		print result

