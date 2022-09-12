from Crypto.Cipher import AES
import hashlib
import random


with open("pass.txt") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
print(hashlib.md5(keyword.encode()).digest())
