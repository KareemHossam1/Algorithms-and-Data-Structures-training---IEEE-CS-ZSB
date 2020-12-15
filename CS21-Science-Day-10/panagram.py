num = int(input())
string = input().lower()
frequency = [0] * 26
for character in string:
    frequency[ord(character)-97] += 1
if all(frequency):
    print('YES')
else:
    print('NO')
