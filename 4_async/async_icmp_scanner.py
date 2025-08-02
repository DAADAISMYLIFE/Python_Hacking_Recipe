from time import time
"""
이 스크립트는 주어진 네트워크 범위에 대해 비동기 ICMP 스캔을 수행합니다.
함수:
    async_func(): 대상 네트워크의 모든 IP 주소에 비동기 핑을 수행하고 결과를 출력합니다.
    do_ping(ip): 주어진 IP 주소에 비동기 핑을 수행하고 결과를 반환합니다.
변수:
    target_network (str): CIDR 표기법으로 된 대상 네트워크 범위.
    net4 (IPv4Network): 대상 네트워크에서 생성된 IPv4 네트워크 객체.
    ip_address (list): 대상 네트워크의 모든 IP 주소 목록.
실행:
    스크립트는 비동기 ICMP 스캔의 실행 시간을 계산합니다.
"""

import asyncio
from pythonping import ping
import ipaddress
from functools import partial

target_network = "100.100.100.0/24"
net4 = ipaddress.ip_network(target_network)
ip_address = []

for ip in net4.hosts():
    ip_address.append(str(ip))
    
async def async_func():
    print(f"목표 네트워크 : {target_network}")
    
    # 고수준 코드
    loop = asyncio.get_running_loop()
    cos = [asyncio.create_task(do_ping(ip)) for ip in ip_address]
    results = await asyncio.gather(*cos)
    
    # 저수준 코드
    # ensure_future: 각 IP 주소에 대해 do_ping 코루틴을 실행하고 Future 객체를 반환
    # futures = [asyncio.ensure_future(do_ping(ip)) for ip in ip_address]
    # # gather: 모든 Future 객체를 동시에 실행하고, 모든 작업이 완료될 때까지 기다림
    # results = await asyncio.gather(*futures)
    
    for result in results:
        if result["Echo Reply"]:
            print(result)
            
async def do_ping(ip):
    # 동기로 작성된 ping 함수를 비동기 코루틴으로 감쌈
    # 키워드 인자 전달을 허용하지 않아서 partial 사용
    loop = asyncio.get_event_loop()
    ping_request = partial(ping, ip, timeout=1, count=1)
    # run_in_executor: 동기 함수를 비동기적으로 실행
    resp = await loop.run_in_executor(None, ping_request)
    return {
        "IP" : ip,
        "Echo Reply" : resp._responses[0].success,
        "Verbose" : resp._responses[0]
    }
    
if __name__ == "__main__":
    begin = time()
    
    # 고수준
    asyncio.run(async_func())
    
    # 저수준
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(async_func())
    # loop.close()
    
    end = time()
    print(f"실행 시간 : {end - begin}")

