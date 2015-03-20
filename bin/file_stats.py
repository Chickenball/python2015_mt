#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	print >>sys.stderr, "Usage of program: {} <filename>".format(__file__)
	sys.exit("Please try again")

def file_stats(input_file):
    lines = 0
    words = 0
    characters = 0
    for line in input_file:
        lines += 1
        for word in line.split():
            words += 1
        for char in line:
            characters += 1
    print lines, words, characters, input_file.name
try:
	filename = open(sys.argv[1])
	file_stats(filename)
except IOError as error:
	print >>sys.stderr, "Failed to open:", filename