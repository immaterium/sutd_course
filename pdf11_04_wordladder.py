import pickle
# Using the pythonds package to test out a ready-made graph package
from pythonds.graphs import Graph

def build_graph(words):
	dictionary = {}
	g = Graph()
	for word in words:
		for i in range(len(word)):
			group = word[:i] + '_' + word[i+1:]
			if group in dictionary:
				dictionary[group].append(word)
			else:
				dictionary[group] = [word]
	for group in dictionary.keys():
		for word1 in dictionary[group]:
			for word2 in dictionary[group]:
				if word1 != word2:
					g.addEdge(word1,word2)
	return g

# This is to load the list of words
with open("words_list.pickle","rb") as f:
	words = pickle.load(f)

# this is to generate the graph
g = build_graph(words)

# This is to store the graph into another pickle object
import sys
sys.setrecursionlimit(0x100000)
with open("graph.pickle", "wb") as f:
	pickle.dump(g, f)
