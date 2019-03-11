import requests
'''请求参数为字典形式'''
# payload={'key1':'value1','key2':'value2'}
# r=requests.get("http://httpbin.org/get", params=payload)
# print(r.url)
'''请求参数为字典形式，请求参数含数组'''
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r=requests.get("http://httpbin.org/get", params=payload)
# print(r.url)
# print(r.content)
# print(r.json)
'''post请求传递一个字典'''
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)
'''post请求传递一个元祖'''
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
# print(r.headers)

payload = {'key1': 'value1', 'key2': 'value2'}
url0="http://httpbin.org/get"
r=requests.get(url=url0, params=payload)
# print(r.url)
print (r.text)
# print (type(r.text))
print(r.status_code)
print(r.headers)
