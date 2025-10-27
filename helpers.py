import requests

def load_html(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html = file.read()
    except:
        try:
            html = requests.get(path).text
        except:
            print('Failed to load from path/URL.')
            return

    return html

def extract_string(original, start_snippet, end_snippet, inclusive=True):
    if inclusive:
        start_i = original.find(start_snippet)
        end_i = original.find(end_snippet) + len(end_snippet)
    else:
        start_i = original.find(start_snippet) + len(start_snippet)
        end_i = original.find(end_snippet)
    return original[start_i:end_i]
