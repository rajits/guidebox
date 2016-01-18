import ast, requests

def get_dict(url):
    f = requests.get(url)

    return ast.literal_eval(f.text)
