#!/usr/bin/python3
"""
Checks that a student cloned the AirBnB_clone_v2 repo in their
web-01 server.
"""
import sys

from fabric import Connection
from io import StringIO
from paramiko import RSAKey


host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]

rsa_key = RSAKey.from_private_key(open(rsa_key_file))
output = StringIO()

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run("ls | grep AirBnB_clone_v2 | tr -d '\n'", shell="/bin/bash", out_stream=output, warn=True)
    print(output.getvalue(), end="")