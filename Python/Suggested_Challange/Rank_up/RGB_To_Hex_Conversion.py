def rgb(r, g, b):
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    r = hex(r).replace("0x","").upper()
    g = hex(g).replace("0x","").upper()
    b = hex(b).replace("0x","").upper()
    if len(r) == 1:
        r = "0" + r
    if len(g) == 1:
        g = "0" + g
    if len(b) == 1:
        b = "0" + b
    return r + g + b

# other solution by users
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num

def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
