import sys
import socket


def connect():
    args = sys.argv
    ip_addr = args[1]
    port = int(args[2])
    message = args[3]

    with socket.socket() as sock:
        sock.connect((ip_addr, port))
        encoded_message = message.encode()
        sock.send(encoded_message)
        buffer = 1024
        response = sock.recv(buffer)
        decoded = response.decode()
        print(decoded)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()
