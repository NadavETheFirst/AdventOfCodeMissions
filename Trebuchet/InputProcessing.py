# part 1-
# This code need to take the inputs.txt and for each line take the first digit and the last digit as a 2 digit numbers and sum all of them.
# exp.:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# part 2-
# needs to acount for digits spelled as words - two1nine is 29 and not 11 like part 1

# ------------

# replaces all instenced of a digit spelled as a word in the actual digits 
def replaceDigitWords(inputString):
    digit_words = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                   "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    digits = {"zero","one","two","three","four","five","six","seven","eight","nine"}
    
    outputString = ""
    starts = "zottffssen"
    for i in range(len(inputString)):
        char = inputString[i]
        if(char.isdigit):
            outputString +=char
        else: 
            if(char == 'z'):
                if(len(inputString)>i+4):
                    for j in range(i,len(inputString)):
                        print("")
                        

    return outputString

def find_occurrences(string1, string2):
    occurrences = []
    index = string1.find(string2)
    while index != -1:
        occurrences.append(index)
        index = string1.find(string2, index + 1)
    return occurrences

# get the value of the string acourding to the defined mission
def getValueFrom(LineInput):
    LineInput = replaceDigitWords(LineInput)
    firstDig = 0
    for chars in LineInput:
        if chars.isdigit():
            firstDig = int(chars)
            break
    lastDig = firstDig
    for chars in reversed(LineInput):
        if chars.isdigit():
            lastDig = int(chars)
            break
    return (firstDig*10) +lastDig


with open('inputs.txt','r') as inputs:
    lines = inputs.read().lower().split("\n")

inputtt = "rtwonenineqxvbgtj4"

i = 0
sum = 0
for line in lines:
    i += 1
    #numberReplaced = replace_digit_words(line)
    value = getValueFrom(line)
    sum+=value
    print(f"Line number {i} is: {line +","+" "*(75-len(line))} value: {value}")
    
print(f"the sum is {sum}")