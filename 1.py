import sys
import bs4
import requests
import webbrowser

def search(productUrl):
    http = "https://127.0.0.1:80"
    https = "http://127.0.0.1:80"

    proxy = { 
        "http"  : http, 
        "https" : https, 
    }

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)'}
    res=requests.get(productUrl, headers=headers, proxies=proxy)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    linkedelement=soup.select('.r a')
    linkstoopen=min(5,len(linkedelement))
    for i in range(linkstoopen):
        webbrowser.open('https://google.co.in'+linkedelement[i].get('herf'))

sea=search('https://google.co.in/search?q='+''.join(sys.argv[1:]))