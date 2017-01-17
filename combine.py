#####################################
# nadine lessio 
# IMAD - Position
# Manifesto proto sentence program
# because sometimes automating your thought process is better for your brain.
# quick and dirty
######################################
"""
structures to follow:

[verb] the [noun] in [noun]				0
[verb] [verb] to [verb] the [noun]		1
[verb] the [noun]						2
[verb] over the [adj] [noun]			3

[verb] in [noun]						4
[verb] to [verb] [noun]					5	
[adj] [verb] through [adj][verb]		6
[adj][noun] should be the way forward	7
[verb] the [noun] into the [adj] [noun]	8

"""

import random
from textblob import Word
import time
import sys


adjectives = ["beautiful","stupid","delicate","intricate","robust","futile","absurd","harmful","political","reductive","destructive","minimal","silly","amusing","ridiculous"]
verbs = ["break","convert","subvert","automate","iterate","destroy","build","compose","expose","remix"]
nouns = ["hive","glitch","device","future","past","agenda","time","usage","system"]


def get_words(v,n,a,s):
	""" This function takes from the lists of various words and returns a dictionary of words ya gonna use for your manifesto """

	verbList = []
	nounList = []
	adjList = []

	if v !=0:
		for i in range(v):
			#print(random.choice(verbs))
			verbList.append(random.choice(verbs))
	if n !=0:
		for i in range(n):
			nounList.append(random.choice(nouns))
	if a!=0:
		for i in range(a):
			adjList.append(random.choice(adjectives))

	#print(verbList)
	#print(nounList)
	#print(adjList)

	dictOfLists = {"verbs":verbList,"nouns":nounList,"adjs":adjList}
	#print(dictOfLists)
	
	make_scentance(dictOfLists,s)


def make_scentance(d,s):
	""" Explode the dict into the scentance you desire """
	
	#print("structure: {0}".format(s))
	#print(d)
	verbs = d['verbs']
	nouns = d['nouns']
	adjs = d['adjs']
	if s == 0:
		#[verb] the [noun] into [noun]	
		print("{0} {1} into the {2}".format(verbs[0],nouns[0],nouns[1]))
	
	elif s == 1:
		#[verb] [verb] to [verb] the [noun]
		print("{0} {1} to {2} the {3}".format(verbs[0],nouns[0],verbs[1],nouns[1]))
	
	elif s == 2:
		#[verb] the [noun]	
		print("{0} the {1}".format(verbs[0],nouns[0]))
	elif s == 3:
		#[verb] over the [adj] [noun]
		print("{0} over the {1} {2}".format(verbs[0],adjs[0],nouns[0]))
	elif s == 4:
		## SUPER GOOD KEEP ###
		#[verb] the [noun]
		print("{0} the {1}".format(verbs[0],nouns[0]))
	elif s == 5:
		#[verb] to [verb] [noun]
		print("{0} to {1} {2}".format(verbs[0],verbs[1],nouns[0]))	
	elif s == 6:
		#[adj] [verb] through [adj][verb]
		print("{0} {1} through {2} {3}".format(adjs[0],verbs[0],adjs[1],verbs[1]))
	elif s == 7:
		#[adj][noun] should be the way forward
		w = Word(nouns[0])
		print("{0} {1} should be the way forward".format(adjs[0],w.pluralize()))
		
	elif s == 8:
		#[verb] the [noun] into the [adj] [noun]
		w = Word(nouns[0])
		o = Word(nouns[1])
		print("{0} {1} into {2} {3}".format(verbs[0],w.pluralize(),adjs[0],o.pluralize()))

	
def choose_structure():
	""" chose the structure randomly. """

	strcutre = random.choice(range(0,8))
	#print("structure: {0}".format(strcutre))

	if strcutre == 0:
		get_words(1,2,0,0) # one verb two nouns
	elif strcutre == 1:
		get_words(2,2,0,1) # three verbs one noun
	elif strcutre == 2:
		get_words(1,1,0,2) #one verb one noun
	elif strcutre == 3:
		get_words(1,1,1,3) #1:v 1:n 1:adj
	elif strcutre == 4:
		get_words(1,1,0,4) # 1v 1n 0adj
	elif strcutre == 5:
		get_words(2,1,0,5) # 1v 1n 1adj
	elif strcutre == 6:
		get_words(2,0,2,6) #2v 0n 2adj
	elif strcutre == 7:
		get_words(0,1,1,7) #1v 0n #1adj
	elif strcutre == 8:
		get_words(1,2,2,8) #1v 2n 2adj

tick = 0

while 1:

	choose_structure()
	time.sleep(2)
	tick +=1
	if(tick == 10):
		sys.exit()



