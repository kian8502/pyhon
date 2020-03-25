from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

top = soup.select("div.hotissue_mini > ol > li")

for e in top:
    link = e.find("a")
    print(link.string +" :", link.get("href"))
