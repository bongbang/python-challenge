from helpers import read_text, cprint
import re

lines = read_text('5_banner.p',
                  'http://www.pythonchallenge.com/pc/def/banner.p').splitlines()

for line in lines:
    if re.search(r'p\d+', line):
        print() # start new line w/ each serial position number
        if line[0] == 'p':
            color = 'blue'
        elif line[:2] == '(l':
            color = 'red'
        elif line[:2] == 'aa':
            color = 'magenta'
        else:
            color = None
    else:
        print(' ', end='')
        if line[-2:] == 'g2':
            color = 'red'
        elif line[-2:] == 'g6':
            color = 'blue'
        else:
            color = None
    cprint(line, color=color, end='')
print() # to start new line in shell
