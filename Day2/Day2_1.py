import math

def parse_input(filename):
    text = open(filename, "r").read()
    textArray = text.split(",")
    for i in range(len(textArray)):
        textArray[i] = textArray[i].split("-")
    return textArray

array = parse_input("./Advent2025/Day2/Day2.txt")
sum = 0
for entry in array:
    start = int(entry[0])
    startDigits = len(str(start))
    end = int(entry[1])
    
    if startDigits % 2 != 0:
        startDigits += 1
        start = 10 ** (startDigits / 2 - 1) * (10 ** (startDigits / 2) + 1)
        
    n = math.ceil(start / (10 ** (startDigits/2) + 1))
    value = n * (10 ** (len(str(n))) + 1)
    while  value <= end:
        sum += value
        n += 1
        value = n * (10 ** (len(str(n))) + 1)
        
        
print(sum)
    