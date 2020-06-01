# import requests
# param ={"q":"西游记"}
# r = requests.get("http://www.douban.com/search", params=param)
#
# print(r.status_code)
# print(r.url)
# print(r.text)



import  requests
param = {"q":"西游记"}
r = requests.get("http://www.baidu.com/search", params = param)
print(r.status_code)