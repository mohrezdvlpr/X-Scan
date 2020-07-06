import requests
from bs4 import BeautifulSoup

urls = []
tries = 0
class CRAWLER:
    

    
    def __init__ ():
        pass
    def rem_dup(ls):
        l2 = []
        for l in ls :
            if not(l in l2):
                l2.append(l)
        return l2
    
    
    def crawl(url,page):
        global urls,tries
        if urls == []:
            try:
                src = requests.get(url).text
            except:
                print("[!] Network Error")
                CRAWLER.crawl(url,page)
            soup = BeautifulSoup(src,'html.parser')
            for i in range(len(soup.find_all('a'))):
                u = str(soup.find_all('a')[i].get('href'))
                if not(u.startswith('http')):
                    u = url +'/'+ u
                if url in u :
                
                    urls = CRAWLER.rem_dup(urls)
                    if len(urls) <= int(page):
                        urls.append(u)
                    else :
                        return urls
        urls = CRAWLER.rem_dup(urls)
        for u in urls :
            try:
                src = requests.get(u).text
            except:
                CRAWLER.crawl(url,page)
            soup = BeautifulSoup(src,'html.parser')
            for i in range(len(soup.find_all('a'))):
                u = str(soup.find_all('a')[i].get('href'))
                if not(u.startswith('http')):
                    u = url +'/'+ u
                if url in u:
                    urls = CRAWLER.rem_dup(urls)
                    if len(urls) <= int(page):
                        urls.append(u) 
                    else:
                        return urls
        tries += 1 
        if tries >= 5:
            return urls
        CRAWLER.crawl(url,page)
        
            
         
        
        
        
        
        