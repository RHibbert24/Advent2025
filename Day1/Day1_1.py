class Lock:
    def __init__(self, startingNumber: int,maxNumber: int):
        if startingNumber > maxNumber:
          raise Exception("Starting number may not be greater than max number")
        self.currentNumber = 50
        self.maxNumber = maxNumber
    
    def turn(self, direction: str, amount: int) -> int:
        if direction == 'L':
            nextNumber = self.currentNumber - amount
        elif direction == 'R':
            nextNumber = self.currentNumber + amount
        else:
            raise Exception("Direction must be either 'L' or 'R'.")
        self.currentNumber = nextNumber % (self.maxNumber + 1)
        return self.currentNumber

lock = Lock(50, 99)
password = 0
with open("./Inputs/Day1.txt") as file:
    for line in file:
        command = line.rstrip()
        value = lock.turn(command[0], int(command[1:]))
        if value == 0:
            password += 1
print(password)