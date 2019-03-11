import  requests
base_url='http://httpbin.org'
param_data={'user':'zxw','password'='666'}
r=requests.get(base_url+'/get',params=param_data)
print(r.url)
print(r.status_code)
qq