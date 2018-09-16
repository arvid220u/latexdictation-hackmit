
import requests
import urllib
import pexpect

APPID="V5KXEA-HL5T9LY4T7"

from shuntington import evaluate
from shuntington import lineareval

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
        ('equals','='),
        ('squared','^2'),
        ('cubed','^3'),
        ('zero','0'),
        ('one','1'),
        ('two','2'),
        ('three','3'),
        ('four','4'),
        ('five','5'),
        ('six','6'),
        ('seven','7'),
        ('eight','8'),
        ('nine','9'),
        ('greater than','>'),
        ('less than','<'),
        ('< or equal to','<='),
        ('> or equal to','>='),
        (' alpha ',' \\alpha '),
        (' beta ',' \\beta '),
        (' gamma ',' \\gamma '),
        (' zeta ',' \\zeta '),
        (' eta ', ' \\eta '),
        (' theta ', ' \\theta '),
        (' iota ',' \\iota  '),
        (' kappa ',' \\kappa  '),
        (' lambda ',' \\lambda  '),
        (' mu ',' \\mu '),
        (' nu ',' \\nu '),
        (' xi  ',' \\xi '),
        (' pi ', ' \\pi '),
        (' rho ', ' \\rho '),
        (' tau ',' \\tau  '),
        (' upsilon ',' \\upsilon '),
        (' phi ',' \\phi '),
        (' chi ',' \\chi '),
        (' psi ',' \\psi '),
        (' omega ',' \\omega '),
]
commonerrors=[
        (' see ',' c '),
        (' some ',' sum '),
        (' end ',' n '),
        (' hey ',' a '),
        (' day ',' a '),
        (' be ',' b '),
        (' overbyte ',' over b '),
        (' for all ',' forall '),
        (' frale ',' forall '),
        (' richer ',' greater '),
        (' is ',' '),
        (' there exists ',' exists '),
        (' there exist ',' exists '),
        (' equivalent to ',' equiv '),
        (' equal to ',' equals '),
        (" I'm ",' n '),
        (' clothes ',' close '),
        (' for ',' four '),
        (' dan ',' then '),
        (' done ',' then '),
        (' such that ',' then '),
        (' we get ',' then '),
        (' whole ',' close '),
        (' closed ',' close '),
        (' cosign ',' cosine '),
        (' sign ',' sine '),
        (' quotes ',' close '),
        (' oakland ',' open '),
        (' and ',' n '),
        (' eggs ',' x '),
        (' clubs ',' close '),
        (' eclipse ',' a plus '),
        (' aid ',' a '),

]

def replace_symbols(text):
    text = " " + text + " "
    for s in commonerrors:
        text=text.replace(s[0], s[1])
    for s in mathSymbols:
        text=text.replace(s[0], s[1])
    return text.lower()



def text2latex(text):
    text=text.lower().replace('some', 'sum')
    print(text)
"""
    r=requests.get("http://api.wolframalpha.com/v2/query?appid="+APPID+"&format=minput&output=json&async=0.1&input="+urllib.parse.quote_plus(text)).json()
    print(r)
    try:
        m = r["queryresult"]["pods"][0]["subpods"][0]["minput"]
        process = pexpect.spawn("wolfram -rawterm")
        process.expect_exact(":=")
        process.sendline('TeXForm[HoldForm['+m+']]')
        process.expect("//TeXForm= .*")
        response = process.after.strip()[len("//TeXForm= "):-len("In[2]:")].strip()
        return response
    except:
        return ' '
"""
    #text=text.replace(' ', '')
    text=replace_symbols(text)
    print(text)

    text=lineareval(text)

    #text=evaluate(text)
    print(text)
    return text

