import string


data = open("../17.txt")
a = [i for i in data]
alphabet = ' ' + string.digits + string.ascii_uppercase
pair_count = 0
summary = set()
for x in range(len(a) - 1):
    for y in range(x + 1, len(a)):
        sys_x = alphabet.index(max(a[x]))
        sys_y = alphabet.index(max(a[y]))
        if abs(sys_x - sys_y) <= 2:
            pair_count += 1
            summary.add(int(a[x], sys_x) + int(a[y], sys_y))
print(pair_count, max(summary))
