#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 12
# Taras Sotnikov

import networkx as nx
import sys

def read_edge(G):
	node1, node2 = sys.stdin.readline().strip().split()
	if node1 != node2:
		if node1 not in G.nodes():
			G.add_node(node1)
		if node2 not in G.nodes():
			G.add_node(node2)
		if len(G.predecessors(node2)) == 0:
			G.add_edge(node1, node2)

def clean_graph(G):
	for node in G.nodes():
		if len(G.predecessors(node)) == 0:
			if len(G.neighbors(node)) == 0:
				G.remove_node(node)

def find_source(G):
	for node in G.nodes():
		if len(G.predecessors(node)) == 0:
			return node

def find_end_nodes(G):
	end_nodes = []
	for node in G.nodes():
		if len(G.neighbors(node)) == 0:
			end_nodes.append(node)
	return end_nodes

def path_len_to_end_nodes(G, start, end_nodes):
	result = []
	for end in end_nodes:
		if nx.has_path(G, start, end):
			result.append(nx.shortest_path_length(G, start, end))
		else:
			result.append(0)
	return sorted(result)


GA = nx.DiGraph()

N = int(sys.stdin.readline())
for i in range(N-1):
	read_edge(GA)

clean_graph(GA)
sourceA = find_source(GA)

#spread path lengths to end nodes
spread = {}
for node in GA.nodes():
	spread[node] = path_len_to_end_nodes(GA, node, find_end_nodes(GA))

#path lenghts from source to all nodes
from_source = {}
for node in GA.nodes():
	from_source[node] = nx.shortest_path_length(GA, sourceA, node)


T = int(sys.stdin.readline())
for n_case in range(1, T+1):
	GB = nx.DiGraph()

	for i in range(N-1):
		read_edge(GB)
	
	clean_graph(GB)
	sourceB = find_source(GB)
	end_nodes_B = find_end_nodes(GB)
	spread_sourceB = path_len_to_end_nodes(GB, sourceB, end_nodes_B)

	if spread[sourceA] != spread_sourceB:
		print "Case #%d: NO" % n_case
	else:
		gb_nodes = GB.nodes()
		ga_nodes = GA.nodes()

		from_source_B = {}
		for node in gb_nodes:
			from_source_B[node] = nx.shortest_path_length(GB, sourceB, node)

		spread_B = {}
		for node in gb_nodes:
			spread_B[node] = path_len_to_end_nodes(GB, node, end_nodes_B)

		gb_nodes.sort()
		ga_nodes.sort()
		ga_nodes.remove(sourceA)
		gb_nodes.remove(sourceB)
		result = [sourceA + "/" + sourceB]
		
		for nodeA in ga_nodes:
			eq_node = None
			for nodeB in gb_nodes:
				if from_source[nodeA] == from_source_B[nodeB]:
					if spread[nodeA] == spread_B[nodeB]:
						eq_node = nodeB
						break
			
			gb_nodes.remove(eq_node)
			result.append(nodeA + "/" + eq_node)

		print "Case #%d: %s" % (n_case, " ".join(sorted(result)))