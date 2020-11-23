s = int(input(), 2)
train = 0
missed = 0
while 4 ** train < s:
    missed += 1
    train += 1
print(missed)
