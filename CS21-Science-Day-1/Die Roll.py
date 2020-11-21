from fractions import Fraction
yak = max(list(map(int, input().split())))
if yak == 1:
    print('1/1')
else:
    print(Fraction((7-yak), 6))
