import requests
url = "https://httpbin.org/post"
payload = {"username":"191899179@qq.com","password":"password"}
response = requests.post(url=url,data=payload)
print(response.status_code)
print(response.text)