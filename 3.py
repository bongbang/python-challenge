from helpers import read_text, extract_string
import re

string = read_text('challenge_3.html')
string = extract_string(string, 'kAewtloYg', 'btSipiqBd')

matches = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', string)
# Fails to find ABCxDEF at start or end of string, but we know that none is
# to be found in *this* string.

print(''.join([m[4] for m in matches]))
