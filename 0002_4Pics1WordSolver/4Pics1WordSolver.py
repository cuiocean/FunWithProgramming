#!/usr/bin/python 
#coding:utf-8
"""
This program will search for all the words of the required length
that can be contructed out of the given letters. 

@author: Haiyang Cui
"""
__doc__ = 'Solve 4Pic1Word programmatically'

def file_to_list(file):
    """ Convert a file to list of words """
    lines = []
    with open(file, 'r') as f:
        lines = f.readlines()
    words = [line.strip() for line in lines]
    return words

def in_subset(word, choices):
    """ Check if the `word` is a subset of `choices`
    """
    choices = list(choices)
    for c in word:
        if c not in choices:
            return False
        choices.remove(c)
    return True	
	
if __name__ == "__main__":
    # Get the required number of letters
	lengthOfWord = input("How long is the word you're looking for: ")

	# Get the letters  
	inputLetters = input("Please enter all the letters : ")
	
	# Load in the word list from a dictionary database
	words = file_to_list('words.txt')
	
	candidates = []
	for word in words:
		if len(word) == int(lengthOfWord):
			if in_subset(word, inputLetters):
				candidates.append(word)
	print("Got ", len(candidates), " word candidates:")
	for word in candidates:
		print(word) 
