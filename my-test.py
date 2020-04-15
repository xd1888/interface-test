import common

mytest = common.Common()
rest = mytest.get("/")
print(rest.text)


"""myPost"""
uri = '/login'
username = 'criss'
password = 'criss'
mytest = common.Common()
payload = "username=" + username + "&password=" + password
content = mytest.post(uri,parameter=payload)
print(content.text)
