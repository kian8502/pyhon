import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://ssl.pstatic.net/tveta/libs/"

centerUrl = "1269/1269170/0ed4f26aaa0acc6f8a6d_20191213183214816.jpg"
sideUrl = "1264/1264712/45223a0f0a344a47269c_20191231101931659.jpg"

savePath1 = "D:/Documents/Python/section2/center.jpg"
savePath2 = "D:/Documents/Python/section2/side.jpg"

f1 = req.urlopen(url + centerUrl).read()
f2 = req.urlopen(url + sideUrl).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f1)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("Complete")
