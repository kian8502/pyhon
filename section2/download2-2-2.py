import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "http://blogfiles.naver.net/20150823_231/codn9_14403263840439uB4A_JPEG/tumblr_n0forjSMuW1qgyg6yo1_540.jpg"
htmlUrl = "https://google.com"

savePath1 = "D:/Documents/Python/section2/test1.jpg"
savePath2 = "D:/Documents/Python/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()
saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료")
