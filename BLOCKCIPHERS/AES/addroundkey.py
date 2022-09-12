state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    decrypt = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    for i in range(len(s[0])):
        for j in range(len(s)):
            decrypt[i][j] = s[i][j] ^ k[i][j]
    return decrypt


decrypt = add_round_key(state, round_key)
flag = ''
for list in decrypt:
    for y in list:
        flag += chr(y)
print(flag)
