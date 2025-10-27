from helpers import read_text

url_stub = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

for number in ['12345', '8022']:
    while all([char.isdigit() for char in number]):
        string = read_text(url_stub + number)
        print(string)
        number = string.split()[-1]
    else:
        print()
