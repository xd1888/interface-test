import requests
url_index = 'http://127.0.0.1:12356/'
url_login = 'http://127.0.0.1:12356/login'
response_index = requests.get(url_index)
print("Respose的内容："+ response_index.text)

username = 'criss'
password = 'criss'

payload = 'username=' + username +'&password=' + password
print(payload)
response_login = requests.post(url_login,data=payload)
print("response_login 内容"+ response_login.text)