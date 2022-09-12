import math


def extended_gcd(p, q):
    if p == 0:
        return q, 0, 1
    else:
        gcd, u, v = extended_gcd(q % p, p)
        return gcd, v - (q // p) * u, u


# Greatest Common Divisor
print("Greatest Common Divisor-----------")
a = 66528
b = 52920
print(math.gcd(a, b))

# Extended GCD
print("Extended GCD---------------")
p = 26513
q = 32321
gcd, u, v = extended_gcd(p, q)
print("crypto{", u, ",", v, "}")

# Modular Arithmetic 1
print("Modular Arithmetic 1----------")
# a = b mod c => a mod c = b

a = 8146798528947
n = 17
if math.gcd(a,n) == 1:
    print (1)

# Modular Arithmetic 2
print("Modular Arithmetic 2---------")
p = 65537
print("answer: ", pow(273246787654, p-1, p))

# Modular Inverting
print("Modular Inverting---------")
# a^(p-1) = 1 (mod p) <=>
# a^(p-2) * 1 = a^-1 (mod p)
a = 3
p = 13
print("answer: ", pow(a, p-2, p))
