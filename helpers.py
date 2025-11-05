import requests

def read_text(*paths):
    '''Read text from path or URL'''
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
        except:
            try:
                text = requests.get(path).text
            except:
                print(f'FAILED to load from {path}')
                continue
        return text

def extract_string(original, start_snippet, end_snippet, inclusive=True):
    '''Extract string at between markers'''
    if inclusive:
        start_i = original.find(start_snippet)
        end_i = original.find(end_snippet) + len(end_snippet)
    else:
        start_i = original.find(start_snippet) + len(start_snippet)
        end_i = original.find(end_snippet)
    return original[start_i:end_i]

def cprint(*args, color=None, **kwargs):
    colors = {'red': 91, 'green': 92, 'yellow': 93, 'blue': 94,
              'magenta': 95, 'cyan': 96}
    if color:
        print(f'\033[{colors[color]}m', end='')
        print(*args, **kwargs)
        print('\033[0m', end='')
    else:
        print(*args, **kwargs)
