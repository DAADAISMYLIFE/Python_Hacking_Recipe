# whois_crawling.py
# whois를 이용하여 DNS와 IP에 대한 정보 획득하는 프로그램

import whois # pip install python-whois
import socket

url = "hakhub.net"

try:
    url_info = whois.whois(url)
    ip = socket.gethostbyname(url) # DNS에서 IP를 획득
    print("=" * 50)
    print("<<URL Info>>")
    print(url_info)
    
    ip_info = whois.whois(ip)
    print("=" * 50)
    print("<<IP Info>>")
    print(ip_info)
# 등록되지 않은 도메인의 경우 예외 발생
except whois.parser.PywhoisError:
    print("Unregistered")