from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")
a = {"div": "slider_container"}
#rec = soup.findAll(a)
rec = soup.select("div.slider_container")
#print(rec)
#print(lec)

for e in rec:
    print(e.select("a href"))
