data = open("../17-361.txt")
a = [int(i) for i in data]
min_sort = sorted(a)
k = 0
min_num = 0
indexes = []
counter = 0

while True:
    min_num = min_sort[k]
    if min_num % 100 == 40:
        break
    k += 1
for i in range(2, len(a)):
    e1 = a[i]
    e2 = a[i - 1]
    e3 = a[i - 2]
    if e1 > min_num and e2 > min_num and e3 > min_num:
        if e2 == e3 != e1:
            indexes.append(a.index(e1) + 1)
            counter += 1
        if e1 == e3 != e2:
            indexes.append(a.index(e2) + 1)
            counter += 1
        if e1 == e2 != e3:
            indexes.append(a.index(e3) + 1)
            counter += 1
        continue
        
print(counter, max(indexes))
