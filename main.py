import requests
from bs4 import BeautifulSoup
from modules.crawl import CRAWLER
from modules.sqli import SQLI
from modules.xss import XSS
import argparse


banner = """
#Banner
"""


def main():
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='url', dest='target')
    parser.add_argument('-p', '--page', help='page', dest='page')
    args = parser.parse_args()

    
    target = args.target
    page = args.page
    print('##################Crawling Started.##################')
    urls = CRAWLER.crawl(target,page)
    for url in urls:
        print(url)
    print('##################Crawling Ended.##################')
    print('##################XSS Scan Started.################')
    for url in urls:
        if '?' in url: 
            vuln = XSS.xss_get(url)
            if vuln :
                print('[+] Found vulnerable URL: ')
                for v in vuln :
                    print(v)
    print('##################XSS Scan Ended.##################')
    print('##################SQLI Scan Started.###############')
    for url in urls:
        if '?' in url: 
            vuln = SQLI.sql_get(url)
            if vuln :
                print('[+] Found vulnerable URL: ')
                for v in vuln :
                    print(v)
    print('##################SQLI Scan Ended.#################')
    




if __name__ == "__main__":
    main()