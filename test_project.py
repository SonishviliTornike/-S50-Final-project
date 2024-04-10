from project import *

def test_checking_url_phishing():
    url_details = {
        'Ai_model_phishing_predict_score': '10.00 %',
        'Ai_model_phishing_risk_class': 'High',
        'DNS_Record': True,
        'Domain Age Risk': 'Low',
        'IP Address in the URL': False,
        'TinyURL': False,
        'Url Reputation': 'Good',
        'bruteforce login attack blacklisted': False,
        'ip blacklisted': False,
        'ssh attack blacklisted': False,
        'Redirection in URL Risk': 'Medium',
        'Low Web_Traffic Risk': 'Medium',
    }

    result = checking_url([url_details])

    expected_result = [
        "\nFalse=Safe/True=Unsafe\n",
        "Ai_model_phishing_predict_score: 10.00 %",
        "Ai_model_phishing_risk_class: High",
        "DNS_Record: True",
        "Domain Age Risk: Low",
        "IP Address in the URL: False",
        "Is Shortened URL: False",
        "Url Reputation: Good",
        "Bruteforce login attack blacklisted: False",
        "Ip blacklisted: False",
        "Ssh attack blaclisted: False",
        "Redirection in URL Risk: Medium",
        "Low Web_Traffic Risk: Medium",
        "THIS URL IS SAFE!",  # Adjusted to indicate that the URL is safe
        "\n-----------------------------------------------------------------------------------------------------------------------\n"
    ]

    assert result == expected_result

def test_ip_check():
    ip_api_response = {
        'result': {
            'ipAddress': '127.0.0.1',
            'isVpn': False,
            'isBruteForce': False,
            'isProxyHttp': False,
            'isZombie': False,
            'isPotentialZombie': False,
            'isDDos': False,
            'isOpenDns': False,
            'isWorm': False
        }
    }
    
    expected_output = [
    "\nTrue=Safe/False=Unsafe\n",
    "IP address: 127.0.0.1",
    "Is VPN: False",
    "Is Brute Force ATTACK Mode: False",
    "Is Proxy Tunnel: False",
    "Is This IP Infected: False",
    "Is This IP is Potential Infected:False",  # Removed the space before the colon
    "Is This IP is DDoS ATTACK Mode: False",
    "Is IP is Open DNS: False",
    "Is IP Trojan WORM: False"
    ]


    result = ip_check(ip_api_response)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


