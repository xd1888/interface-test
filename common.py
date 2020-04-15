import requests
class Common:
    def __init__(self):
        self.url_root='http://127.0.0.1:12356'
    

    def get(self,uri,parameter=""):
        Myurl = self.url_root+uri+parameter
        response_index = requests.get(Myurl)
        return response_index
    
    def post(self,uri,parameter=""):
        Myurl = self.url_root+uri
        if len(parameter) > 0:
            res = requests.post(Myurl,data=parameter)
        else:
            res = requests.post(Myurl)
        return res




