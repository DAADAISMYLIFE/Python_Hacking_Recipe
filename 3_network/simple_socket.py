from socket import *
import os
def parsing(host):
    if os.name == "nt":
        sock_protocol=IPPROTO_IP
    else:
        sock_protocol=IPPROTO_ICMP
    
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))
    
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)
        
    data = sock.recvfrom(65535)
    print(data)
    print(data[0])
    
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_OFF)
        
    sock.close()
    
if __name__ == "__main__":
    host = "118.38.140.164"
    print(f"Listening at [{host}]")
    parsing(host)
        