import listener
from pwn import *
import json
import base64
import codecs
from binascii import unhexlify


r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(101):
    received = json_recv()
    if "flag" in received: 
        print(received["flag"])
        break
    print("debug", received)
    encoded = received["encoded"]
    type = received["type"]
    if type == "base64":
        decoded = base64.b64decode(encoded).decode('utf8').replace("'", '"')
    elif type == "hex":
        decoded = (unhexlify(encoded)).decode('utf8').replace("'", '"')
    elif type == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif type == "bigint":
        decoded = unhexlify(encoded.replace("0x", "")).decode('utf8').replace("'", '"')
    elif type == "utf-8":
        decoded = ""
        for i in encoded:
            decoded += chr(i)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

listener.start_server(port=13377)
