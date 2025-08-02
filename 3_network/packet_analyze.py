from socket import *
import os
import struct

def parsing(host):
    if os.name == "nt": # 운영체제가 windows면
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
        
    # 소켓 생성
    my_sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    my_sock.bind((host, 0))
    
    my_sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    
    if os.name == "nt":
        my_sock.ioctl(SIO_RCVALL, RCVALL_ON)
        
    packet_number = 0
    
    try:
        while True:
            packet_number+=1
            data=my_sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_ip_header(data[0])
            
            print(f"{packet_number} 번째 패킷")
            print(f"전체 헤더 : {ip_headers}")
            print(f"버전 : {ip_headers[0] >> 4}")
            print(f"헤더 길이 : {ip_headers[0] & 0x0F}")
            print(f"서비스 타입 : {ip_headers[1]}")
            print(f"총 길이 : {ip_headers[2]}")
            print(f"확인 :  {ip_headers[3]}")
            print(f"IP 플래그, 프래그먼트 오프셋 {flags_and_offset(ip_headers[4])}") 
            print(f"생명 시간 : {ip_headers[5]}")
            print(f"프로토콜 : {ip_headers[6]}")
            print(f"헤더 체크섬 : {ip_headers[7]}")
            print(f"출발지 주소 : {inet_ntoa(ip_headers[8])}")
            print(f"목적지 주소 : {inet_ntoa(ip_headers[9])}")
            print(f"페이로드 : {ip_payloads}")
            print("=" * 50)
            
            
    except KeyboardInterrupt:
        if os.name == "nt":
            my_sock.ioctl(SIO_RCVALL, RCVALL_OFF)
            my_sock.close()
            
    
    
def parse_ip_header(ip_header):
    ip_header=struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payload = ip_header[20:]
    return ip_header, ip_payload

def flags_and_offset(int_num):
    byte_num = int_num.to_bytes(2, byteorder="big")
    x=bytearray(byte_num)
    flags_and_flagment_offset = bin(x[0])[2:].zfill(8)+bin(x[1])[2:0].zfill(8)
    return(flags_and_flagment_offset[:3], flags_and_flagment_offset[3:])



if __name__ == "__main__":
    host = "118.38.140.164"
    print(f"Listening at [{host}]")
    parsing(host)