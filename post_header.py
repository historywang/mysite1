import  requests
import json
url = "https://httpbin.org/post"
header = {"Content-Type": "application/x-www-form-urlencoded",
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", }
response = requests.post(url=url ,headers=header,verify=False)#verify=False 表示忽略ssl的证书
print(response.status_code)
print(response.text)
print(response.json())