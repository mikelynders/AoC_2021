import os

def readT(textFile = str):

    file = open(textFile, 'r')

    text = file.read()

    textList = [x for x in text.split('\n')]

    file.close()

    return textList