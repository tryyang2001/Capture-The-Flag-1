"""
Someone just sent Grandma Susan'oo a new message...
encrypted.txt is produced by the output of main.py
What are the properties of OTP? (compare the differences between encryption and decryption)
Is there a way to find out the original key used?
"""
print("\nInsecure OTP")
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

encrypted = "faa4a0ba8d435a2b2015c4625c80443e820c523a9ee190baa2504d20640cca2e6bd54e30990b533ac6e1adf5ea4157243d58d22b7b9d1732950b6d3dddb5b6e9a25e4b64642fcd3b2f915e3bcc52522092a2abf5ba11422a310a852a6a94537f83451d21daa4f9feb8505c2a2a568b6c2fb6646ddd1b0a2efd9589d59e616475300895367faa656c9c185c21edaaeae395000e1a320dc92c3c87563d804e40"
msg = "Hey Grandma Susan'oo, I have told you not to play with my Photoshop! \
Why did you crop your head on the dragon... "
key = xor(msg.encode()[0:20], bytearray.fromhex(encrypted)[0:20])
print(key)

def decrypt(msg, key):
    res = b""
    for i in range(0, len(msg), 20):
        res += xor(key, msg[i:i+20])
    return res.decode('ascii', 'ignore')

print(decrypt(bytearray.fromhex(encrypted), key))