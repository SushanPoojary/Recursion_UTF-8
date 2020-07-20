import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline() #reads one line

	if line:
		print_line(line, encoding, errors) #executes print_line function
		return main(language_file, encoding, errors) #Recursive function


def print_line(line, encoding, errors):
	next_lang = line.strip() #remove beginning and end characters
	raw_bytes = next_lang.encode(encoding, errors = errors) #encode string
	cooked_string = raw_bytes.decode(encoding, errors = errors) #decode bytes
	print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = 'UTF-8')

main(languages, encoding, error) #Execution starts here

#input: Sublime.py UTF-8 strict
#OP: hex values are visible \x and the ones not supported show boxes in cooked strings
# You DBES i.e Decode Bytes and Encode Strings