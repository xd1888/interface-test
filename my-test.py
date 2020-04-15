import common

mytest = common.Common()
rest = mytest.get("/")
print(rest.text)

rest = mytest.post()