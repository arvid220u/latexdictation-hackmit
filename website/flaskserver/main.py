from shuntington import evaluate

mathSymbols=[
        ('plus', '+'),
        ('minus', '-'),
        ('over', '/'),
        ('divided by', '/'),
        ('divide', '/'),
        ('times', '*'),
        ('by', '*'),
        ('open', '('),
        ('close', ')'),
]

def replace_symbols(text):
    for s in mathSymbols:
        text=text.replace(s[0], s[1])
    return text

def text2latex(text):
    print(text)
    text=text.replace(' ', '')
    text=replace_symbols(text)
    print(text)
    text=evaluate(text)
    print(text)
    return text
