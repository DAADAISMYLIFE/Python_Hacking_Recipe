# ping_sweep.py
# 일정 IP 범위를 흽쓸고 지나가면서 ICMP Echo Request를 확인하여 존재의 유무를 확인하는 스크립트

from pythonping import ping
from time import time

def icmp_scan():
    ip_addresses = ["33.22.143.1", "8.8.8.8", "google.com"]
    for ip_address in ip_addresses:
        print(f"Ping Target=>{ip_address}")
        ping(ip_address, timeout=1, count=1, verbose=True)
        
if __name__ == "__main__":
    begin=time()
    icmp_scan()
    end=time()
    print(f"실행 시간 : {end-begin}")