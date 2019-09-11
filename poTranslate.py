# - *- coding: utf- 8 - *-
import getopt
import sys
import os
import time
import polib
from googletrans import Translator

#Print the help of the script
def usage():
	helptext = 'poTranslate\n\n'
	helptext = helptext + 'This script translates the different texts of a .po file into the language that the user wants. \n'
	helptext = helptext + 'Parameters:\n'

	helptext = helptext + '-p --inputFile : Input File with extension .po \n'
	helptext = helptext + '-i --ISO : The language to translate the source text into. The value should be one of the language codes listed in googletrans.LANGUAGES or one of the language names listed in googletrans.LANGCODES. \n'
	helptext = helptext + '-v --version : Software version \n'
	helptext = helptext + '-h --help : Print this help \n\n'
	helptext = helptext + ".poTranslate (c) Bioversity International, 2019\n"
	helptext = helptext + "Author: Brandon Madriz. b.madriz@cgiar.org / bmadriz@mrbotcr.com"
	print(helptext)

# Main function
def main():
	#Obtain the comamnd line arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h:p:i:v", ["help","inputFile=",  "ISO=", "version="])
	except getopt.GetoptError as err:
		print(str(err)) #If there is an error then print it
		usage() #Print the help
		sys.exit(1) #Exits with error

	if len(opts) == 0:
		usage() #Print the help
		sys.exit(1) #Exits with error

	inputFile = ""
	iso = ""
	#This for statement gets each command line argument and fill avobe variables
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-p", "--inputFile"):
			inputFile = a
		elif o in ("-i", "--ISO"):
			iso = a
		elif o in ("-v", "--version"):
			print("poTranslate 1.0")
		else:
			assert False, "unhandled option"

	try:
		translator = Translator()
		po = polib.pofile(inputFile)
		
		lenUnTranslated = len(po.untranslated_entries() + po.fuzzy_entries())
		print ("Let's translate: "+str(lenUnTranslated)+" strings.")
		time.sleep(2)
		counter = 0
		for entry in po.untranslated_entries() + po.fuzzy_entries():
			try:
				entry.msgstr= translator.translate(entry.msgid, dest='es').text
			except:
				entry.msgstr = ""

			counter = counter +1

			#print "Processing entry : #"+str(counter)
			print ("Processed entries: "+str((counter*100)/lenUnTranslated), end="\r")

		print (str(po.percent_translated())+"% of string translation completed.")
		po.save()
		
	except:

		sys.exit(1)

#Load the main function at start
if __name__ == "__main__":
	main()