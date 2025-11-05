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
