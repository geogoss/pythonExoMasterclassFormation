
def get_binary_from_char(c):
    return "{0:07b}".format(ord(c))

def get_binary_from_str(s):
    result = ""
    for c in s:
        result += get_binary_from_char(c)
    return result

def generate_cn_encoding_for_sequence(c, count):
    s = ""
    if c == "1":
        s = "0 "
    else:
        s = "00 "

    s+= "0" * count
    return s


def generate_cn_encoding(b):
    c = b[0]
    count = 1
    seq = ""
    for i in range(1, len(b)):
        if b[i] == c:
            count += 1
        else:
            #print("Sequence", c, count)
            if len(seq) > 0:
                seq += " "
            seq += generate_cn_encoding_for_sequence(c, count)
            c = b[i]
            count = 1
    if len(seq) > 0:
        seq += " "
    seq += generate_cn_encoding_for_sequence(c, count)
    return seq

# % = 37 = 0100101


binary = get_binary_from_str("%")
print(binary)
print(generate_cn_encoding(binary))
