from dataclasses import replace

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def findA(list):
    for element in list:
        if len(element) == 3: str1 = element
        if len(element) == 2: str2 = element
    
    for c in str1:
        if c in str1 and c not in str2: return c

def findB(list):
    for letter in letters:
        appearances = 0
        for element in list:
            if letter in element: appearances += 1
        if appearances == 6: return letter

def findC(list, dictionary):
    for letter in letters:
        appearances = 0
        for element in list:
            if letter in element: appearances += 1
        if appearances == 8 and letter != dictionary['a']: return letter

def findD(list):
    for element in list:
        if len(element) == 4: myStr = element
    for letter in letters:
        appearances = 0
        for element in list:
            if letter in element: appearances += 1
        if appearances == 7 and letter in myStr: return letter

def findE(list):
    for letter in letters:
        appearances = 0
        for element in list:
            if letter in element: appearances += 1
        if appearances == 4: return letter

def findF(list):
    for letter in letters:
        appearances = 0
        for element in list:
            if letter in element: appearances += 1
        if appearances == 9: return letter

def findG(list):
    for element in list:
        if len(element) == 4: myStr = element
    for letter in letters:
        appearances = 0
        for element in list:
            if letter in element: appearances += 1
        if appearances == 7 and letter not in myStr: return letter

def stringToDigit(string):
    switcher = {"abcefg": 0, 
                "cf": 1,
                "acdeg": 2,
                "acdfg": 3,
                "bcdf": 4,
                "abdfg": 5,
                "abdefg": 6,
                "acf": 7,
                "abcdefg": 8,
                "abcdfg": 9}
    return switcher.get(string, "nothing")

def get_key(val, dictionary):
    for key, value in dictionary.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def translate(list, dictionary):
    translatedList = []
    for element in list:
        translated = [get_key(x, dictionary) for x in element]
        result = ''.join(translated)
        translatedList.append(result)
    return translatedList

def formNumber(list):
    n = len(list)
    s = 0
    for i in range(n):
        s = s + pow(10, n - 1- i) * list[i]
    return s

with open('input.txt') as file:
    dictionary = {}
    result = 0
    for line in file.readlines():
        #dictionary.clear()
        #print(dictionary)
        data = line.split('|')
        info = data[0].strip().split(' ')
        goalNumberOriginal = data[1].strip().split(' ')
        #print(goalNumberOriginal)

        dictionary['a'] = findA(info)
        dictionary['b'] = findB(info)
        dictionary['c'] = findC(info, dictionary)
        dictionary['d'] = findD(info)
        dictionary['e'] = findE(info)
        dictionary['f'] = findF(info)
        dictionary['g'] = findG(info)

        #print(dictionary)

        goalNumberTranslated = translate(goalNumberOriginal, dictionary)
        #print(goalNumberTranslated)
        goalNumberTranslatedSorted = [''.join(sorted(x)) for x in goalNumberTranslated]
        digitsList = [stringToDigit(x) for x in goalNumberTranslatedSorted]
        #print(digitsList)
        #print(formNumber(digitsList))
        result = result + formNumber(digitsList)
           
    print(result)