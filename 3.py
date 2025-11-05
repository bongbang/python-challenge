from helpers import read_text, extract_string
import re

string = read_text('challenge_3.html')
string = extract_string(string, 'kAewtloYg', 'btSipiqBd')

matches = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', string)
# Woud not find ABCxDEF at start or end of string, but we know that none is
# to be found in *this* string, so this is fine. To make this robust would
# be non-trivial b/c of re's fixed-width look-behind:
# https://stackoverflow.com/a/40617321/1493867

print(''.join([m[4] for m in matches]))
