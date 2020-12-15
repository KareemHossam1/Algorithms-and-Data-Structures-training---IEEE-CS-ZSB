from operator import add
first = input()
second = input()
check = input()
frequencyF = [0] * 26
frequencyS = [0] * 26
frequencyC = [0] * 26
for character in first:
    frequencyF[ord(character)-65] += 1
for character in second:
    frequencyS[ord(character)-65] += 1
for character in check:
    frequencyC[ord(character)-65] += 1
if list(map(add, frequencyF, frequencyS)) == frequencyC:
    print('YES')
else:
    print('NO')
