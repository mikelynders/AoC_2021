import os
from readTxt import readT as rT

textList = rT('gammaInput2.txt')


def isBitGreater(numList, bitOrder, majority):
    sum = 0

    for num in numList:

        sum += int(num[bitOrder])

    if (sum/len(numList) >=.5 and majority) or ((sum/(len(numList)) < .5) and (not majority)):
        return 1
    else:
        return 0

bitCount = len(textList[0])
gamma = 0
epsilon = 0

for x in (range(bitCount)):
    gamma += isBitGreater(textList, x, True)*2**(bitCount-1-x)
    epsilon += isBitGreater(textList, x, False)*2**(bitCount-1-x)
    print('gamma: ', gamma, 'eps: ', epsilon)


print('answer: ', epsilon*gamma)

a = ('a','b','c')

print(enumerate(a))






