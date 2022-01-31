"""
Create a function that returns current working directory, username and IP address as a tuple.
Then call the function and print out the returned values.

*EXAMPLE*
CWD: C:\Users\ozren.tk\Dokumenti\VUA\PIP\work\workshops
Hostname: ZG-VUA-JOHN
IP address: 192.168.100.123
"""
import os
import socket

def get_config():
    cwd = os.getcwd()
    host = socket.gethostname()
    ipaddr = socket.gethostbyname(host)
    return (cwd, host, ipaddr)

cwd, host, ipaddr = get_config()
print(f"CWD: {cwd}")
print(f"Hostname: {host}")
print(f"IP address: {ipaddr}")
