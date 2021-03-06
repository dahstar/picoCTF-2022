#-------------------------------------------------------------
encrypted_flag = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_8F7GK99J"
a, b, g, p = 7, 3, 5, 13
#-------------------------------------------------------------

import string

letters = string.ascii_uppercase + string.digits

key, mod = pow(g, a*b, p), len(letters)
flag = ""

for char in encrypted_flag:
    if char in letters:
        flag += letters[(letters.index(char) - key) % mod]
    else:
        flag += char

print("picoCTF{" + flag + "}")

# picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_3A2BF44E}