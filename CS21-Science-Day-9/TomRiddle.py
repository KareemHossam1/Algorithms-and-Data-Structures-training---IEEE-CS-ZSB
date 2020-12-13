names = []
for i in range(int(input())):
    names.append(input())
for name in range(len(names)):
    if names[:name+1].count(names[name]) > 1:
        print('YES')
    else:
        print('NO')
