import os.path


def readlistoffiles():
	#import pdb; pdb.set_trace()
	Listsoffiles = open("Files.txt","r")
	Array_name = []
	for line in Listsoffiles:
		line = line.strip("\n")
	return printingoffile(line)
	#return ("successfull printing")



def printingoffile(line):
		out_open_file = open(line,"r")
		out_read_file = out_open_file.read()
		return out_read_file	
		
readlistoffiles()

