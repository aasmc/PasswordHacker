import sys
import socket
import string
import itertools

alphabet = string.ascii_lowercase
numbers = [str(x) for x in range(0, 10)]
max_attempts = 1_000_000
allowed_tokens = list(itertools.chain(alphabet, numbers))


def get_password():
    for i in range(1, len(allowed_tokens)):
        for p_word in itertools.product(allowed_tokens, repeat=i):
            yield ''.join(p_word)


def connect():
    args = sys.argv
    ip_addr = args[1]
    port = int(args[2])

    with socket.socket() as sock:
        sock.connect((ip_addr, port))
        num_attempts = 0
        buffer = 1024
        password_generator = get_password()
        p = ""
        while num_attempts <= max_attempts:
            message = next(password_generator)
            encoded_message = message.encode()
            sock.send(encoded_message)
            response = sock.recv(buffer)
            decoded = response.decode()
            if decoded == "Connection success!":
                p = message
                break
            num_attempts += 1
        print(p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()
