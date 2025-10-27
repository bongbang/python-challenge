from helpers import load_html

url_stub = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

for n in ['12345', '8022']:
    while all([char.isdigit() for char in n]):
        string = load_html(url_stub + n)
        print(string)
        n = string.split()[-1]
    else:
        print()
