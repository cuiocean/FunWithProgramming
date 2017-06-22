#!/usr/bin/python
# coding:utf-8
"""
This program reads in the CSV file, provide the option to manipulate per line
of the file and save the modified data into a new CSV file.

Usage:
    ManipulateCSVFile.py input.csv

@author: Haiyang Cui
"""

import sys
from pathlib import Path
 
def main(argv):
	if len(sys.argv) != 2:
		sys.exit("Usage: ManipulateCSVFile.py input.csv")
	inputFile = argv[1]
	m_file = Path(inputFile)
	if not m_file.exists():
		sys.exit("The input file does not exist.")

	print('The input file is ' + inputFile)
	ManipulateCSVFile(inputFile)

 
def ManipulateCSVFile(inputFile):
	print("Processing the csv file....")
	import csv
	import os
	head, tail = os.path.split(inputFile)
	
	newFileName=""
	if head == "":
		newFileName="Modified_" + tail
	else:
		newFileName =  head +"\Modified_" + tail;
	
	with open(newFileName,'wt',newline='') as resultFile:
		wr = csv.writer(resultFile, dialect='excel')
		reader = csv.reader(open(inputFile, "rt"))
		for row in reader:
			if not row:
				continue
			newRowData = ManipulateRowData(row)
			wr.writerow(newRowData)
	print("The data has been saved to file: " + newFileName)
	print("Done!!")
	
# This is just an example of how to manipulate the row data.
def ManipulateRowData(rowData):
	newRowData=[]
	for i in range(len(rowData)):
		cellData = rowData[i]
		if cellData == "Nunavut":
			newRowData.append("ExampleData")
		else:
			newRowData.append(cellData)	
	return newRowData
			
if __name__ == "__main__":
	main(sys.argv)