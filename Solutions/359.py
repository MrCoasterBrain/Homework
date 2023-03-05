count = 0
sums = []
with open("../17-354.txt") as s:
    data = [int(i) for i in s]
    for i in range(1, len(data)):
        if abs(data[i] % 10 - data[i - 1] % 10) == 1:
            if (data[i] % 5 == 0 and data[i - 1] % 5 != 0) or (data[i] % 5 != 0 and data[i - 1] % 5 == 0):
                if data[i] ** 2 + data[i - 1] ** 2 > min([q ** 2 for q in data if q % 10 == 2]):
                    count += 1
                    pair_sum = data[i] + data[i - 1]
                    if pair_sum > 0:
                        sums.append(pair_sum)
print(count, min(sums))
