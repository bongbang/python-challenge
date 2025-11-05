from helpers import read_text

url_stub = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

for nothing in ('12345', '8022'):
    while all(char.isdigit() for char in nothing):
        clue = read_text(url_stub + nothing)
        print(clue)
        nothing = clue.split()[-1]
    else:
        print()
