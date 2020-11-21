data = list(map(int, input().split()))[1]
array = input().split()
for i in range(data):
    array.append(array.pop(0))
for i in array:
    print(i, end=' ')
