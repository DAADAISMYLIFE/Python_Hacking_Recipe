from socket import *
import os
import struct
import sys

def parse_ip_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads

def parse_icmp_header(icmp_data):
    icmp_headers = struct.unpack("!BBHHH", icmp_data[:8])
    icmp_payloads = icmp_data[8:]
    return icmp_headers, icmp_payloads

def parsing(host):
    if os.name == "nt":
        socket_protocol = IPPROTO_IP
    else:
        socket_protocol = IPPROTO_ICMP
        
    sock = socket(AF_INET, SOCK_RAW, socket_protocol)
    sock.bind((host, 0))
    
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)
        
    file_path = "./recv_logo.jpg"
    
    if os.path.isfile(file_path):
        os.remove(file_path)
    receive_bytes = 0
    
    try:
        while True:
            data = sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_ip_header(data[0])
            
            if ip_headers[6] == 1:
                ip_source_address = inet_ntoa(ip_headers[8])
                ip_destination_address = inet_ntoa(ip_headers[9])
                print(f"{ip_source_address} => {ip_destination_address}")
                
                icmp_headers, icmp_payloads = parse_icmp_header(ip_payloads)
                receive_bytes = len(icmp_payloads)
                
                if icmp_headers[0] == 8:
                    print(f"데이터 받는 중... {receive_bytes}")
                    with open(file_path, "ab") as f:
                        f.write(icmp_payloads)
                    
                    if icmp_payloads == b"EOF":
                        print("종료!")
                        sock.ioctl(SIO_RCVALL, RCVALL_OFF)
                        sys.exit(0)
                print("=" * 20)
                
    except KeyboardInterrupt:
        if os.name == "nt":
            sock.ioctl(SIO_RCVALL, RCVALL_OFF)
        sock.close()
    
if __name__ == "__main__":
    host = "118.38.155.112"
    print(f"스니핑 시작 [{host}]")
    parsing(host)