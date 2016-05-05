#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 5
# Taras Sotnikov

import telnetlib
from itertools import chain, imap
from operator import itemgetter
from collections import Counter
import sys

def start_game(tn,all_words):	
	filter_words = all_words

	tn.write("\n")

	text = tn.read_until(">").split("\n")
	entry = text[len(text)-3].strip().replace(" ", "")
	word_size = len(entry)

	filter_words = [word for word in filter_words if len(word) == word_size]

	used_chars = []
	found = False
	for i in range(word_size + 5):
		letter = None
		counter = Counter(chain.from_iterable(imap(set, filter_words)))
		most_common = map(itemgetter(0), counter.most_common())
		for j in range(len(most_common)):
			letter = most_common[j]
			if letter not in used_chars:
				tn.write(letter)
				break;
		
		aux = tn.expect(["GAME OVER","Press enter to continue...",">"])
		if aux[2].find("GAME OVER") != -1:
			restart_connection(tn)
			start_game(tn, all_words)
			sys.exit
		elif aux[2].find("Press enter to continue...") != -1:
			text = aux[2].split("\n")
			for line in text:
				if "key" in line:
					print line
			start_game(tn, all_words)
			sys.exit()
		elif ">" in aux[2]:
			text = aux[2].split("\n")
		else:
			text = aux[2].split("\n")
			for line in text:
				if "key" in line:
					print line
			sys.exit()

		try:
			entry = text[len(text)-3].strip().replace(" ", "")
		except Exception:
			sys.exit()

		for k in range(len(entry)):
			if entry[k] != "_":
				if entry[k] not in used_chars: 
					filter_words = [word for word in filter_words if entry[k] == word[k]]

		used_chars.append(letter)

def restart_connection(tn):
	tn.close()
	tn.open("52.49.91.111",9988,60)
	tn.read_until("Press enter to continue...")

all_words = [line.rstrip() for line in open('words.txt')]

tn = telnetlib.Telnet("52.49.91.111",9988,60)
tn.read_until("Press enter to continue...")
start_game(tn, all_words)