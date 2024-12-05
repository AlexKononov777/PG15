import sys

b = 0
for i in sys.stdin:
    if 'далек' in i:
        for j in i.lower().split():
            if j.lower()[:5] == 'далек':
                b += 1
                break

print(b)