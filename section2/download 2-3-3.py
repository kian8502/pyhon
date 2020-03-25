import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
values = {
    'ctxCd': '1001'
}

print('before',values)
params = urlencode(values)
print('after',params)

url = api + "?" + params

print("request url",url)

reqData = req.urlopen(url).read().decode('utf-8')
print("reqData",reqData)
