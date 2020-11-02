from binascii import unhexlify

def xor(a, b):
    return bytes([a ^ b])

key = unhexlify(b"bcabb984a9b28ca0cb8dcca09ccfcf9382")
flag = b""


for i in key:
    flag += xor(i, 255)

print(flag)
