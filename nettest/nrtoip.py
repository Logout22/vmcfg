from sys import argv

def nrtoip(nr):
    for i in range(4):
        print(nr % 256)
        nr //= 256

def iptohex(ip):
    parts = ip.split(".")
    factor = 1
    result = 0
    for i in range(4):
        result += int(parts[i]) * factor
        factor *= 256
    print(hex(result))

if len(argv) > 2:
    iptohex(argv[1])
else:
    nrtoip(int(argv[1], 0))

