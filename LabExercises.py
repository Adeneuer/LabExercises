#EX 2 6 11

#1
def fib(nums = 100):
    fiblist = []
    fiblist.append(0)
    fiblist.append(1)
    for i in range(2,nums):
       fiblist.append(fiblist[i-2]+fiblist[i-1])
    return fiblist

def main1():
    alist = fib()
    print(alist)

#2
def baseConv(li,b1,b2):
    newList = []
    sumB10 = 0
    for exp in range(len(li)-1,-1,-1):
        if int(li[-1-exp])<b1:
            sumB10+=int(li[-1-exp])*pow(b1,exp)
        else:
            return "Illegal conversion"
    while sumB10:
        newList.insert(0,sumB10%b2)
        sumB10 = int(sumB10/b2)
    return newList

def main2():
    fin = open("thoutgs.txt", 'r')
    r = fin.readlines()
    numList = []
    numList = r[0].split()
    print(baseConv(numList,int(r[1]),int(r[2])))
#...

#6
import string

def processWord(word):
    newWord = word
    for c in word:
        if c not in (string.ascii_letters + string.digits):
            newWord = newWord.replace(c,'',1)
    return newWord

def engToMorse(line,morseToEngDict,engToMorseDict):
    newLine = ""
    words = line.split()
    for word in words:
        word = processWord(word).upper()
        for c in word:
            word = word.replace(c,engToMorseDict[c]+" ",1)
        newLine = newLine + word + "    "
    newLine = newLine.strip(' ')
    return newLine

def morseToEng(line,morseToEngDict,engToMorseDict):
    newLine = ""
    newWord = ""
    words = line.split("     ")
    for word in words:
        chars = word.split(" ")
        for c in chars:
            if c in morseToEngDict:
                newWord = newWord + morseToEngDict[c]
        newLine = newLine + newWord + ' '
        newWord = ""
    return newLine

def main6():
    morseToEngDict = {}
    engToMorseDict = {
        " ": "     ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
    }
    fin = open("things.txt", 'r')
    for x, y in engToMorseDict.items():
        morseToEngDict[y] = x
    for r in fin:
        print(r.strip())
        print(engToMorse(r,morseToEngDict,engToMorseDict))
        print(morseToEng(engToMorse(r,morseToEngDict,engToMorseDict),morseToEngDict,engToMorseDict),end='\n\n')

#7

#...

#11
import math

def isPal(num):
    snum = str(num)
    return snum==snum[::-1]

def findPal():
    pals = []
    for i in range(999,899,-1):
        for j in range(i,899,-1):
            if isPal(i*j):
                pals.append(i*j)
    return max(pals)

def main11():
    print(findPal())

#12

#main1()
#main2()
#main6()
#main11()
