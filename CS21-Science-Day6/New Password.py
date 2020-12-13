import random
inp = list(map(int, input().split()))
alpha = list('abcdefghijklmnopqrstuvwxyz')
letters, password, index = [], '', 0
for i in range(inp[1]):
    letters.append(alpha.pop(alpha.index(random.choice(alpha))))
while len(password) < inp[0]:
    password += letters[index]
    if index == len(letters)-1:
        index = 0
    else:
        index += 1
print(password)
