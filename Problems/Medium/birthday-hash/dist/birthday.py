"""
Grandma Susan'oo has invited you to join her birthday party!

She has a gift for the best joker!

nc cs2107-ctfd-i.comp.nus.edu.sg 4001
"""
print("\nBirthday Hash")
import os
import hashlib
import random
import string
print (1 << 0)
event_hex = "2433076380ef23a5c534c195a663f809f2366947"
event = bytes.fromhex(event_hex)
lookup_table = dict()
seq = [str for str in string.printable if str not in string.whitespace]
for _ in range(2**48):
    random_byte = ''.join(random.sample(seq, 8)).encode()
    result = hashlib.sha512(event + random_byte).digest()[:6]
    if result in lookup_table and random_byte != lookup_table[result]:
        print("One of the possible combination is:")
        temp1 = random_byte.decode('utf-8', "ignore")
        temp2 = lookup_table[result].decode('utf-8', "ignore")
        if (sha512(event + temp1.encode()).digest()[:6] == sha512(event + temp2.encode()).digest()[:6]):
            print(temp1, temp2)
            break
    else:
        lookup_table[result] = random_byte
print("The flag is CS2107{No_h@sh_can_esc4pe_b1rthd@y_p@rad0x}")