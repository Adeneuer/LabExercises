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
        
main6()

