import subprocess
import socket
import sys

hostname = socket.gethostname()
lan     = socket.gethostbyname(hostname)
local   = "127.0.0.1"

host = None
if len(sys.argv) > 1:
    if sys.argv[1] == "local":
        host = local
    elif sys.argv[1] == "lan":
        host = lan

subprocess.run([
    "daphne",
    "-b", host,
    "-p", "8000",
    "chatroom.asgi:application"
])

