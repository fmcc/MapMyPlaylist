import sys

# Greets the person whose name is the argument
def main():
	print 'Hello there', sys.argv[1]
	# Command line args are in sys.argv[1], sysargv[2] ...
	# sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program
if __name__ == '__main__':
	main()