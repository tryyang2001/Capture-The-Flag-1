"""
We've sniffed out some information from RSA encrypted traffic. Can you decode it?
You need to factor the given broken modulus. For this purpose, there are several databases online that could be useful:
126198 501118 389160 989977 983392 586327 (36 digits)
143652 478924 221397 696146 709897 519627 (36 digits)
You subsequently need to obtain the private key by calculating e^-1 mod phi(n) or using Python's inverse() function found in the Crypto library.
With all the pieces to the puzzle, you can decrypt the message via pow(ciphertext, private key d, modulus n).
"""
print("\nPrime Time Question")
cipher = 790720275960851803934057676432939180157671812730674675700641077222428
public_e = 65537
modulus = 18128727522177729435347634587168292968987318316812435932174117774340029
p = 126198501118389160989977983392586327
q = 143652478924221397696146709897519627
assert p*q == modulus
phi = (p - 1) * (q - 1)
mi = pow(public_e, -1, phi)
assert (mi*public_e)%phi == 1
plain = pow(cipher, mi, modulus)
print(plain)
plain = str(hex(plain))
print(plain)
print(bytes.fromhex(plain[2:len(plain)]).decode('utf-8', "ignore"))