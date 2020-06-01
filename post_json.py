import requests
import json
url = "https://httpbin.org/post"
payload = {"username":"191899179@qq.com","password":"password"}
data_json = json.dumps(payload)#json格式化
response = requests.post(url=url,json=data_json)
print(response.text)