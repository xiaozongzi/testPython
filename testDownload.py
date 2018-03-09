import requests
url = 'http://huajun1.onlinedown.net/down/LogViewerPro.zip'
r = requests.get(url)
with open("demo3.zip", "wb") as code:
     code.write(r.content)
