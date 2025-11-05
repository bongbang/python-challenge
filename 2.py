from helpers import read_text, extract_string

page = read_text('2_challenge.html',
                 'http://www.pythonchallenge.com/pc/def/ocr.html')
blob = extract_string(page, '%%$@_$^__', '#@}&$[[%]_')

char_counts = {}
for x in blob:
    char_counts[x] = char_counts.get(x, 0) + 1

sorted_counts = sorted(char_counts.items(), key=lambda item: item[1])

for x in char_counts:
    print(f'{x}: {char_counts[x]}')
