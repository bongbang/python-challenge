from helpers import read_text
import pickle

pickle_str = read_text('5_banner.p',
                  'http://www.pythonchallenge.com/pc/def/banner.p')
pickle_bytes = pickle_str.encode('ascii')
banner = pickle.loads(pickle_bytes)

for x in banner:
    print(x)

for line in banner:
    for char, rep in line:
        print(char*rep, end='')
    print()
