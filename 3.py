from helpers import load_html, extract_string
import re

string = load_html('challenge_3.html')
string = extract_string(string, 'kAewtloYg', 'btSipiqBd')

matches = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', string)
# TODO make more reobust by providing for beginning of/end of string

# TODO change load_html to read_text

print(''.join([m[4] for m in matches]))
