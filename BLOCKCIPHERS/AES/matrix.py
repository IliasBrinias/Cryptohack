def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i + 4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    return bytes(matrix)


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125]
]
flag = ""
for i in matrix:
    for y in i:
        flag += (chr(int(y)))
print("flag : ", flag)
# print(matrix2bytes(matrix))
