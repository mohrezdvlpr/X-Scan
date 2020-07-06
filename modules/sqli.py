import requests
import re


class SQLI:

    def __init__():
        pass
         
    def sql_get(url):
        payloads = ["'", "%5c", "%27%22%28%29", "'><", "%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
        vuln = []
        data = url.split('?')[1].split('&')
        variable = []
        value = []
        for d in data :
             variable = d.split('=')[0]
             value = d.split('=')[1]
        for val in value:
            for payload in payloads:
                try:
                    req = requests.get(url.replace(val,val+payload))
                    if 'SQL ' in req.text:
                        vuln.append(url.replace(val,val+"'"))
                        return vuln
                except:
                    pass
        return
    
    
    def sql_post(url):
        pass
    
