import base64
from Crypto.Util import number


def utf8_to_ascii(list):
    msg = ""
    for i in list:
        msg += chr(i)
    return msg


def base64_to_bytes(text):
    return base64.decode(text)


def long_to_bytes(int):
    return number.long_to_bytes(int)


# ascii
print("ascii------")
list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = ""
for i in list:
    flag += chr(i)
print(flag)

# Hex
print("Hex-----")
flag = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(flag).decode())

# Base64
print("Base64-----")
flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag_bytes = bytes.fromhex(flag)
print(base64.encodebytes(flag_bytes).decode())

# Bytes and Big Integers
print("Bytes and Big Integers-----")
flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag = number.long_to_bytes(flag)
print(flag.decode())