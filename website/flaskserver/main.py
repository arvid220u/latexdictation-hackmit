import requests
import urllib
import pexpect

APPID="V5KXEA-HL5T9LY4T7"

def text2latex(text):
    text=text.lower().replace('some', 'sum')
    print(text)
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
