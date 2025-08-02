from time import time
"""
이 스크립트는 주어진 네트워크 범위에 대해 동기 ICMP 스캔을 수행합니다.
함수:
    sync_func(): 대상 네트워크의 모든 IP 주소에 동기 핑을 수행하고 결과를 출력합니다.
    do_ping(ip): 주어진 IP 주소에 동기 핑을 수행하고 결과를 반환합니다.
변수:
    target_network (str): CIDR 표기법으로 된 대상 네트워크 범위.
    net4 (IPv4Network): 대상 네트워크에서 생성된 IPv4 네트워크 객체.
    ip_address (list): 대상 네트워크의 모든 IP 주소 목록.
실행:
    스크립트는 동기 ICMP 스캔의 실행 시간을 계산합니다.
"""

from pythonping import ping
import ipaddress

target_network = "100.100.100.0/24"
net4 = ipaddress.ip_network(target_network)
ip_address = []

for ip in net4.hosts():
    ip_address.append(str(ip))
    
def sync_func():
    print(f"목표 네트워크 : {target_network}")
    for ip in ip_address:
        result = do_ping(ip)
        if result["Echo Reply"]:
            print(result)
            
def do_ping(ip):
    # 동기 방식으로 ping 함수를 호출
    resp = ping(ip, timeout=1, count=1)
    return {
        "IP" : ip,
        "Echo Reply" : resp._responses[0].success,
        "Verbose" : resp._responses[0]
    }
    
if __name__ == "__main__":
    begin = time()
    sync_func()
    end = time()
    print(f"실행 시간 : {end - begin}")
