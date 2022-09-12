from binascii import unhexlify
from PIL import Image
import numpy as np


def xor_two_hex(s1, s2):
    return ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a, b in zip(s1, s2))


def xor_one_byte(s1, s2):
    flag = "".encode()
    for i in s1:
        flag += bytes([i ^ s2])
    try:
        return flag.decode("utf-8")
    except:
        return "error"


def find_key(input, key):
    flag = "".encode()
    for i in range(len(input)):
        flag += bytes([input[i] ^ key[i]])
    try:
        return flag
    except:
        return "error"


def load_image_to_hex(image_name):
    with open(image_name, 'rb') as f:
        content = f.read().hex()
    return content


def make_key_length(key, length):
    y = 0
    final_key = ""
    for i in range(length):
        final_key += key[y]
        y += 1
        if y == len(key):
            y = 0
    return final_key


# XOR Starter
print("XOR Starter---------------")
flag = ""
for i in "label":
    flag += chr(ord(i) ^ 13)
print('crypto{{{}}}'.format(flag))

# XOR Properties
print("XOR Properties---------------")
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2 = xor_two_hex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", KEY1)
KEY3 = xor_two_hex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", KEY2)
KEY4 = xor_two_hex(xor_two_hex(KEY1, KEY2), KEY3)
FLAG = xor_two_hex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", KEY4)
print(unhexlify(FLAG))

# Favourite byte
print("Favourite byte----------------")
n = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
n = unhexlify(n)
flag = {}
for i in range(256):
    flag[i] = xor_one_byte(n, i)
print(([s for s in flag.values() if "crypto" in s]))

# You either know, XOR you don't
print("You either know, XOR you don't--------------")
n = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(n)
# find the key and xor with that the cipher
key = find_key(cipher[:7], "crypto{".encode()).decode("utf-8") + 'y'
final_key = make_key_length(key, len(cipher))
print(find_key(cipher, final_key.encode()))

# Lemur XOR
print("Lemur XOR----------------")
# load the images and i convert them to bits
i1 = Image.open("flag.png")
i2 = Image.open("lemur.png")
i1bit = np.array(i1)*255
i2bit = np.array(i2)*255

# XOR with Numpy and save the image
result = np.bitwise_xor(i1bit, i2bit).astype(np.uint8)
Image.fromarray(result).save('result.png')
Image.open('result.png').show()

