import requests
import urllib

APPID="V5KXEA-HL5T9LY4T7"

def text2latex(text):
    print(text)
    r=requests.get("http://api.wolframalpha.com/v2/query?appid="+APPID+"&format=plaintext&output=json&async=0.1&input="+urllib.parse.quote_plus(text)).json()
    return r["queryresult"]["pods"][0]["subpods"][0]["plaintext"]
