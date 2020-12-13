s = input()
out = ''
go = True
for i in range(len(s)):
    if go:
        if s[i] == '1':
            out += 'A'
            go = True
        elif s[i+1] == '0':
            out += 'B'
            go = False
        else:
            out += 'C'
            go = False
    else:
        go = True
print(out)
