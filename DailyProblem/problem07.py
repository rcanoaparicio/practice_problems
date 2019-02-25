"""
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def dec_num(message, mem):
    if message in mem:
        return mem[message]
    if len(message) <= 1:
        return 1
    if message[0] == "0":
        return 0
    if message[0] == "1" or message[0] == "2" and int(message[1]) < 7:
        r = dec_num(message[1:], mem) + dec_num(message[2:], mem)
        mem[message] = r
        return r
    else:
        r = dec_num(message[1:], mem)
        mem[message] = r
        return r

memo = {}
print(dec_num("1238711111111111119419283491823741028793411111111111111111876123487612893491111111111111111111111118712398759871239864123412348912349871238764187234876123968741237487612348761872634182973498712534234523424112439876123498712435876123492135", memo))
print(dec_num("12111111111111111111111111111111111111387111111111111194192811111111111111111111111111111111111111111111111111113491823741028793411111111111111111876123487612893491111111111111111111111118712398759871239864123412348912349871238764187234876123968741237487612348761872634182973498712534234523424112439876123498712435876123492131111111111111111111111151", memo))
print(dec_num("2106", memo))
print(dec_num("111", memo))
print(dec_num("603", memo))
print(dec_num("1224", memo))
print(dec_num("12211", memo))
print(dec_num("122111", memo))
print(dec_num("1221111", memo))
print(dec_num("12121212121212121212121212121212121212121212121212121", memo))
