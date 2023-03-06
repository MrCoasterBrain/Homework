import statistics

data = open("../17_5758.txt")
a = [int(i) for i in data]
mode = statistics.mode(a)
cnt = 0
diffs = []
for x in range(len(a)):
    for y in range(x + 1, len(a)):
        if a[y] < mode < a[x] or a[x] < mode < a[y]:
            if abs(abs(x - y) - 1) % 2 != 0:
                cnt += 1
                diffs.append(max(mode - a[x], mode - a[y]))
print(cnt, max(diffs))
