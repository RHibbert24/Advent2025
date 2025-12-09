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
    end = int(entry[1])
    for number in range(start, end + 1):
        stringNumber = str(number)
        digits = len(stringNumber)
        for unitLength in range(1, digits // 2 + 1):
            if digits % unitLength == 0:
                unit = stringNumber[:unitLength]
                if unit * (digits // unitLength) == stringNumber:
                    sum += number
                    break
        
print(sum)
    