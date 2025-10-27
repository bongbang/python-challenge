from helpers import load_html

url_stub = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

for n in ['12345', '8022']:
    while True:
        string = load_html(url_stub + n)
        print(string)
        n = string.split()[-1]
        if not all([char.isdigit() for char in n]):
            print()
            break
