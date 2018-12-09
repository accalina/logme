
#Depedencies
import os
import sys
import logging as log

#Local variable
mypath = os.getcwd()
logname = 'logfile.log'

# Main Module
def main():
	os.system('cls')
	print("Logme - Logging system v1.0 \nCopyright Accalina\n")


	try:
		if sys.argv[1] == 'write':
			writefile()
		elif sys.argv[1] == 'read':
			readfile()
		elif sys.argv[1] == 'clear':
			clearlog()
		else:
			print("argument is not valid")
	except:
		print(
			"Please provide arguments!\n"+
			"_________________________\n"+
			"read  : reading logfile\n"+
			"write : write logfile\n"+
			"clear : clear logfile\n"
		)	
	
# Subroutine Modules
def userinput():
	userinput = input("Please input test Strings: ")
	return userinput

def writefile():
	print("Writting Log...")
	log.basicConfig(level=log.DEBUG,
					format='%(asctime)s %(levelname)-8s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename=logname)

	log.info("this is INFO Log")
	log.warning("this is WARNING Log")
	log.error("this is ERROR Log")
	log.debug("this is DEBUG Log")
	print('Log has been saved on {}\{}'.format( mypath,logname ))

def readfile():
	try:
		if sys.argv[2] != '':
			print('Reading {}\{}'.format( mypath,logname ))
			logfile = open(logname).read().split('\n')
			for row in logfile:
				if (sys.argv[2]).upper() in row:
					print(row)
			
	except:
		print('Reading {}\{}'.format( mypath,logname ))
		logfile = open(logname).read().split('\n')
		for row in logfile:
			print(row)

def clearlog():
	logfile = open(logname,'w')
	logfile.write("")
	logfile.close()
	print("Log on {}\{} has been cleared".format( mypath,logname ))

if __name__ == '__main__':
	main()
