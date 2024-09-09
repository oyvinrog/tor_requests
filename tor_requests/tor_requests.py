""" 
This script is used to control the tor proxy.

wrapper for get and post requests with tor proxy

"""
import requests
from colorama import Fore, init
import ipwhois

__port = 9150
__proxies = {
    'http': f'socks5://127.0.0.1:{__port}',
    'https': f'socks5://127.0.0.1:{__port}'
}

def show_whois(ip):
    results = ipwhois.IPWhois(ip).lookup_rdap()
    
    country = results.get('asn_country_code')
    description = results.get('asn_description')
    print(f'{ip} is {description} and is in {country}')

def get(url, **kwargs):
    print(f'Getting {url} through TOR')
    return requests.get(url, proxies=__proxies, **kwargs)

def post(url, **kwargs):
    print(f'Posting to {url} through TOR')
    return requests.post(url, proxies=__proxies, **kwargs)

def test_tor():
    # Initialize colorama for colored output
    init()

    # Get real IP and WHOIS
    real_ip = requests.get('http://httpbin.org/ip').json()['origin']
    print(f"Real IP: {real_ip}")
    
    try:
        show_whois(real_ip)
    except Exception as e:
        print(f"Error getting real IP WHOIS: {e}")

    # Get IP and WHOIS through TOR
    try:
        tor_ip = get('http://httpbin.org/ip').json()['origin']
        print(f"TOR IP: {tor_ip}")
        
        try:
            show_whois(tor_ip)
        except Exception as e:
            print(f"Error getting TOR IP WHOIS: {e}")

        if real_ip != tor_ip:
            print(Fore.GREEN + "Success! Your IP has changed when using TOR." + Fore.RESET)
        else:
            print(Fore.RED + "Failed! Your IP did not change when using TOR." + Fore.RESET)
    except requests.exceptions.RequestException as e:
        # show stack trace
        print(e)
        print(Fore.RED + "Error: Unable to connect through TOR. Make sure TOR is running." + Fore.RESET)

if __name__ == "__main__":
    test_tor()