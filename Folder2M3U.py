# -*- coding: utf_8 -*-

import os

# Class for handle the FOLDER entity
# Recursively nested objects are generated in the list called CHILDREN
class Folder:
	def __init__(self, dirname, foldername, filename = ""):
		# Save absolute path and name:
		self.path = os.path.join(dirname,foldername) 
		self.foldername = foldername
		# "filename" is the name for the M3U file to be generated (i.e. usually the artist name at least at the first level)
		# At the top of the tree (the first execution, the ROOT folder) the filename is "(first)"
		# That indicates to reset the filenames inheritance and set the current folder value in the second level of the tree
		if filename == "":
			# If filename is empty (fist execution) is set the flag value "(first)"
			self.filename = "(first)"
		elif filename == "(first)":
			# If is set the "(first)" value, this is the second (Artist level)
			# Inheritance is reset and the correct value is the current folder (the Artist name)
			self.filename = self.foldername
		else:
			# In other case, the filename is inherited from the father + current folder
			self.filename = filename + " - " + self.foldername

		# Reset buffer
		self.filelinesbuffer = []
		#Reset children
		self.children = []

	def scan (self):
		# Walk through the directory
		for item in os.listdir(self.path):
			# MP3 files are appended to buffer
			if os.path.isfile(os.path.join(self.path,item)):
				if item.split(os.extsep)[-1] == "mp3" and item[0] != ".":
					self.filelinesbuffer.append(item)
			# If the element is a folder, RECURSIVITY!
			elif os.path.isdir(os.path.join(self.path,item)):
				# Add the child to the object:
				self.children.append(Folder(self.path,item,self.filename))
				# Scan the newly added child, this is the RECURSIVE CALL:
				self.children[-1].scan()
				# Sort the list of lines of the newly added child (already scanned):
				# A lambda function is used for sort according to the numbers that appears before the song names. 				
				# FirstElement() function is used for get the first element according to a series of separators
				self.children[-1].filelinesbuffer = sorted(self.children[-1].filelinesbuffer, key=lambda item: (int(FirstElement(item)) if item[0].isdigit() else float('inf'), item))
				# If the newly added child...
				#	... is an "album" (2 inheritance levels, contains " - ") 
				#	... has more than one child (is an artist with two or more albums)				
				if (self.children[-1].filename.find(" - ") > -1 or len(self.children[-1].children) != 1):
					# Save the file:
					self.children[-1].SaveFile()
				# In other cases It is not necessary to create a M3U file, that would double (artist list and his only album)				
		# Concatenate the children M3U files:				
		for child in self.children:
			for item in child.filelinesbuffer:
				self.filelinesbuffer.append(os.path.join(child.foldername,item))

	def SaveFile(self):
		if (len(self.filelinesbuffer)>0):		
			# Open/create file:
			f = open(os.path.join(self.path, self.filename + ".m3u"), "w")
			# Write the concatenated buffer with break lines (\n)
			f.writelines("\n".join(self.filelinesbuffer))
			# Close the file:
			f.close


def FirstElement(input):
	# Example: INPUT "01 - Name of the Song.mp3" > OUTPUT > "01"
	# Returns the first element
	separators = [' ','.','-','_','>','|','/','\\']
	for item in separators:
		input = input.partition(item)[0]
	return input
	

def DeleteM3UFolder (dirname):
	# Delete M3U files of a folder (and subfolders)
	import fnmatch 	# for regexp translation
	import re 		# for regexp
	# File extensions to be deleted (it could be a list)
	includes = ['*.m3u']
	# Translate extensions to regular expressions:
	includes = r'|'.join([fnmatch.translate(x) for x in includes])
	# Walk through the directory:
	for root, dirs, files in os.walk(dirname):
		# The files list has not absolute paths:
		files = [os.path.join(root, f) for f in files]
		# Select files that match the regular expression:
		files = [f for f in files if re.match(includes, f)]
		# Remove!
		for fname in files:			
			os.remove(fname)

def DeleteHiddenFilesFolder (dirname):
	# Delete hidden/temporary files that starts by "."
	import re
	# Regular expression:
	expresionreg = "^\..*"
	# Walk through the directory:
	for root, dirs, files in os.walk(dirname):
		# Same method that "DeleteM3UFolder()"
		files = [os.path.join(root, f) for f in files if re.match(expresionreg, os.path.split(f)[-1])]
		# Remove!
		for fname in files:
			os.remove(fname)			


def AskForYesNoOption (text):
	AnswerYes = "YESyesYes"
	AnswerNo = "NnNONono"
	Answer = "_"
	while((AnswerYes + AnswerNo).find(Answer) < 0):
		Answer = str(raw_input(text + " (Y/N) > "))
	return (AnswerYes.find(Answer) > -1) and (AnswerNo.find(Answer) == -1)

### --------------------------------###		
###     The program starts here     ###

if __name__ == "__main__":	
	while(1):
		# Ask for the root execution folder
		rootfolder = str(raw_input("What is the root folder to start conversion? (or write \"cancel\") \n> "))
		if rootfolder == "cancel":
			break
		elif (os.path.exists(rootfolder)):
			# Ask for extra options:
			deleteMP3 = AskForYesNoOption("Delete existing M3U files?")
			deleteHidden = AskForYesNoOption("Delete hidden files? (ie. \".extension\")")
			# Delete if applicable:
			if (deleteMP3):
				DeleteM3UFolder(rootfolder)
			if (deleteHidden):
				DeleteHiddenFilesFolder(rootfolder)
			# Split the path and the name of the root folder (to create the object):	
			print("Working on it...")
			splitted_root = os.path.split(rootfolder)
			RootFolder = Folder("".join(splitted_root[:-1]),splitted_root[-1])
			RootFolder.scan()
			print("The End! press ENTER")
			raw_input() # Avoid direct closure
			break
		else:
			print("This is not a folder, please try again:")
