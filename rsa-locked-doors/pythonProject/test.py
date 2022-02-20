import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from itertools import chain, product
from hashlib import sha512

#bruteforce function found online
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

ivhex = "4b0fb9a4dfbabe6810b2fb01d2012b84"
cthex = "c089a2553fdcbb0bbdbd7655fc34c75eb7f2ccd28fc801480c5a15b7f366f8737a30aa3e845d79e509486ffd6aa81a0b"
iv = bytes.fromhex(ivhex)
ct = bytes.fromhex(cthex)

for i in range(10**6):
    print("Finding the correct output...")
    try:
        key = sha512(os.urandom(3)).digest()[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ct)
        flag = unpad(plaintext, AES.block_size)
        print(flag.decode())
        break
    except:
        continue
