import requests
import socket
import json
from pyfiglet import Figlet, figlet_format
from termcolor import colored



class CustomApiError(Exception):
    def __init__(self, message):
        self.message = message


def main():
    url = get_url()
    result = get_api(url)
    if result:
        checked_url = checking_url(result)
        for detail in checked_url:
            print(detail)
    

    answer = questions_func()
    if answer == 'y':
        ip_addr = get_ip(url, answer)
        ip_api = get_ip_checker_api(ip_addr)
        if ip_api != None:
            checked_ip = ip_check(ip_api)
            for detail in checked_ip:
                print(detail)
            print("\nGoodbye...")
        elif ip_api == None:
            print(f"\nAPI request failed, check API endpoint!")
        else:
            print("\nExiting program...")
    else:
        print("\nExiting program...")

def get_url():
    f = Figlet(font='slant')
    print((colored(figlet_format("URLipy\n"), color="red")))
    while True:
        sucipicous_url = input("Enter URL to check with https protocol: ").strip()
        #Checks urls only with https portocol, bug API
        if not sucipicous_url.startswith('https'):
            sucipicous_url = 'https://' +  sucipicous_url
            return sucipicous_url
        elif sucipicous_url.startswith('https://'):
            return sucipicous_url
        else:
            return 'Can\'t check the domain name please enter with https protocol.' 






#This api checks url phishing
def get_api(domain):
    try:  
        url = 'https://phishing-url-risk-api.p.rapidapi.com/url/'

        querystring = {"url":domain}

        headers = {
            "X-RapidAPI-Key": "df23d537a5msh1c3234b7d402299p1718eajsn35796c0ab226",
            "X-RapidAPI-Host": "phishing-url-risk-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()
    except json.JSONDecodeError:
        return "Failed to parse response as JSON:" 




def get_ip(domain, answer):
    if answer:
        try:
            #Domain translator translates only with clear domain, without https protocol.
            if domain.startswith('https://'):
                cleaned_domain = domain.replace('https://', '')
            else:
                cleaned_domain = domain
                
            ip_addr = socket.gethostbyname(cleaned_domain)
            return ip_addr
        except socket.herror:
            return 'No IP address found'
    else:
        return False





def checking_url(url_details):
    url_details_list = []

    url_details_list.append("\nFalse=Safe/True=Unsafe\n")
    url_details_list.append(f"Ai_model_phishing_predict_score: {url_details[0]['Ai_model_phishing_predict_score']}")
    url_details_list.append(f"Ai_model_phishing_risk_class: {url_details[0]['Ai_model_phishing_risk_class']}")
    url_details_list.append(f"DNS_Record: {url_details[0]['DNS_Record']}")
    url_details_list.append(f"Domain Age Risk: {url_details[0]['Domain Age Risk']}")
    url_details_list.append(f"IP Address in the URL: {url_details[0]['IP Address in the URL']}")
    url_details_list.append(f"Is Shortened URL: {url_details[0]['TinyURL']}")
    url_details_list.append(f"Url Reputation: {url_details[0]['Url Reputation']}")
    url_details_list.append(f"Bruteforce login attack blacklisted: {url_details[0]['bruteforce login attack blacklisted']}")
    url_details_list.append(f"Ip blacklisted: {url_details[0]['ip blacklisted']}")
    url_details_list.append(f"Ssh attack blaclisted: {url_details[0]['ssh attack blacklisted']}")
    url_details_list.append(f"Redirection in URL Risk: {url_details[0]['Redirection in URL Risk']}")
    url_details_list.append(f"Low Web_Traffic Risk: {url_details[0]['Low Web_Traffic Risk']}")

    if url_details[0]['Ai_model_phishing_predict_score'] > '10.00 %':
        url_details_list.append("\nTHIS URL IS PHISHING, BY CLICKING ATTACKER WILL KNOW YOUR IP ADDRESS AND CAN TOOK YOUR PASSWORDS!")
    else:
        url_details_list.append("THIS URL IS SAFE!")
    url_details_list.append("\n-----------------------------------------------------------------------------------------------------------------------\n")

    return url_details_list






def questions_func():
    try:
        check_ip = input("\nDo you want to check this IP address to? (y/n): ").strip().lower()

        if check_ip != "y" and check_ip != "n":
            return questions_func()
        else:
            raise ValueError
    except ValueError:
        return "Nothing to check"




#This api works fast and good :)

def get_ip_checker_api(ip_addr):
    try:
        if ip_addr:
            print(f"These IP address/addresses {ip_addr} are associated with the domain, and they are used to route traffic to the appropriate server hosting the content for that domain.")
            url ="https://netdetective.p.rapidapi.com/query"

            querystring = {"ipaddress": ip_addr}

            headers = {
                "X-RapidAPI-Key": "df23d537a5msh1c3234b7d402299p1718eajsn35796c0ab226",
                "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            if response.status_code == 200:
                checked_ip = response.json()
                return checked_ip
            else:
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def ip_check(ip_addr):
    ip_check_list = []

    ip_check_list.append("\nTrue=Safe/False=Unsafe\n")
    ip_check_list.append(f"IP address: {ip_addr['result']['ipAddress']}")
    ip_check_list.append(f"Is VPN: {ip_addr['result']['isVpn']}")
    ip_check_list.append(f"Is Brute Force ATTACK Mode: {ip_addr['result']['isBruteForce']}")
    ip_check_list.append(f"Is Proxy Tunnel: {ip_addr['result']['isProxyHttp']}")
    ip_check_list.append(f"Is This IP Infected: {ip_addr['result']['isZombie']}")
    ip_check_list.append(f"Is This IP is Potential Infected:{ip_addr['result']['isPotentialZombie']}")
    ip_check_list.append(f"Is This IP is DDoS ATTACK Mode: {ip_addr['result']['isDDos']}")
    ip_check_list.append(f"Is IP is Open DNS: {ip_addr['result']['isOpenDns']}")
    ip_check_list.append(f"Is IP Trojan WORM: {ip_addr['result']['isWorm']}")

    return ip_check_list


if __name__ == "__main__":
    main()

