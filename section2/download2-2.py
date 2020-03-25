import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "http://blogfiles.naver.net/20150823_231/codn9_14403263840439uB4A_JPEG/tumblr_n0forjSMuW1qgyg6yo1_540.jpg"
htmlUrl = "https://google.com"

savePath1 = "D:/Documents/Python/section2/test1.jpg"
savePath2 = "D:/Documents/Python/section2/index.html"
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")
