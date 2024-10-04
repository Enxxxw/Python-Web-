import sys

for line in sys.stdin:
    a = line.split()
    if len(a) == int(n[0]):
        res = ' '.join(sorted(a))
        print(res)

