"""
    Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
    repeated successive characters as a single count and character. For example,
    the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

    Implement run-length encoding and decoding. You can assume the string to be encoded
    have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def encode(text):
    result = ""
    count = 1
    for i in range(len(text)):
        if i < len(text) - 1 and text[i] == text[i+1]:
            count += 1
        else:
            result += str(count) + text[i]
            count = 1
    return result

def decode(text):
    result = ""
    i = 0
    while i < len(text):
        n = ""
        while text[i] >= "0" and text[i] <= "9":
            n += text[i]
            i += 1
        n = int(n)
        for _ in range(n):
            result += text[i]
        i += 1
    return result

print(encode("AAAABBBCCDAAF"))
print(decode(encode("AAAABBBCCDAAF")))
print(encode("AAAABBBCsdfgsdfgaaaaaaaaaaaAAFAAAABBBCsdfgsdfgagggggggggggggggggggggggsdfCDaaaaaasdgfagfgaaaaaaaaaaaaAAF"))
print(decode(encode("AAAABBBCsdfgsdfgaaaaaaaaaaaAAFAAAABBBCsdfgsdfgagggggggggggggggggggggggsdfCDaaaaaasdgfagfgaaaaaaaaaaaaAAF")))
