# Password Hacker

Educational project from JetBrains HyperSkill Academy. Level Challenging.

## Stage 1
### Description

Imagine some admin who runs a website on the Internet. The site is becoming very popular, and a lot of people register. Filling in their profiles, they leave some information there that is not meant to be public, for example, information about their credit cards.

The admin completely forgot about the security of the site, so now you can log in with admin privileges without even having a login and password!

The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site. It will get harder: the tasks of all other stages of the project will be to crack the admin password. Good luck!

Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.
### Objectives

Your program will receive command line arguments in this order:

- IP address
- port
- message for sending

The algorithm is the following:

- Create a new socket.
- Connect to a host and a port using the socket.
- Send a message from the third command line argument to the host using the socket.
- Receive the server’s response.
- Print the server’s response.
- Close the socket.

### Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

```text
> python hack.py localhost 9090 password
Wrong password!
```

Example 2

```text
> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
```

## Stage 2
### Description

The admin noticed someone sneaking around the site with admin rights and came up with a password. Now to log in as an admin, you need to enter the password first. Maybe the admin has set a relatively easy and short password so that it is easy to remember? Let's try to brute force all possible passwords to enter the site!

So far the program is very simplistic: it’s time to improve it so that it can generate different variants of the password and then try each one. The admin of the server doesn’t hide the information that passwords vary in length and may include letters from a to z and numbers from 0 to 9. You should start with a,b,c,....,z,0,1,..aa,ab,ac,ad and continue until your password is correct. It’s very important to try all the variants of every length because otherwise your program risks never finding the password!

If the password is correct, you will receive the “Connection success!” message. Otherwise, you will see the “Wrong password!” message. The server cannot receive more than a million attempts, so if your program works indefinitely, you will see the unfortunate message “Too many attempts”.
### Objectives

In this stage, you should write a program that:

- Parses the command line and gets two arguments that are IP address and port.
- Tries different passwords until it finds the correct one.
- Prints the password it found.

Note that you can connect to the server only once and then send messages many times. Don't connect to the server before sending every message.

Also, note that here and throughout the project, the password is different every time you check your code.
### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
```text
> python hack.py localhost 9090
pass
```