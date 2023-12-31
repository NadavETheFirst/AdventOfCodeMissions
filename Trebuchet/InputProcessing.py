# This code need to take the inputs.txt and for each line take the first digit and the last digit as a 2 digit numbers and sum all of them.
# exp.:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

def getValueFrom(LineInput):
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
    lines = inputs.read().split("\n")

firstInput = "lmfkvgfzfmhxqrcvsgt28ssmhm5fivethree"
value = getValueFrom(firstInput)

print(f"value for {firstInput} is {value}")

# i = 0
# for line in lines:
#     i += 1
#     print(f"Line number {i} is: {line}")


