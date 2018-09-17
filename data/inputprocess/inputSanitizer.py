import re
import sys

input = open(sys.argv[1]) 

output = open("kjv.clean.txt", 'a')

for line in input:
	line = re.sub(r'^([A-Z][a-z][a-z0-5]\|[0-9]*\|[0-9]*\|).', "", line)
	line = re.sub(r'(\~)','', line)
	output.write(line)
	
input.close
output.close