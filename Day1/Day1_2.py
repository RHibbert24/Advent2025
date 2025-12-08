class Lock:
    def __init__(self, startingNumber: int,maxNumber: int):
        if startingNumber > maxNumber:
          raise Exception("Starting number may not be greater than max number")  
        self.currentNumber = startingNumber
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
    
    def timesThroughZero(self, direction: str, amount: int) -> int:
        if direction == 'L':
            nextNumber = self.currentNumber - amount
        elif direction == 'R':
            nextNumber = self.currentNumber + amount
        else:
            raise Exception("Direction must be either 'L' or 'R'.")
        
        # For values > 0, occurences of 0 is always value // (max + 1)
        times = abs(nextNumber // (self.maxNumber + 1))

        # For values <= 0, we need to account for where we start and the behaviour of // for negatives.
        if nextNumber <= 0:
            # If we end on a multiple of max + 1, then we have crossed zero once more than expected.
            # e.g. -100 from > 0 should be 2
            if nextNumber % (self.maxNumber + 1) == 0:
                times += 1
            # If we started at 0, then we have hit it one less time than expected.
            # e.g. -101 from 0 should be 1 not 2
            if self.currentNumber == 0:
                times -= 1
        
        self.turn(direction, amount)

        return times

lock = Lock(50, 99)
password = 0
with open("./Inputs/Day1.txt") as file:
    for line in file:
        command = line.rstrip()
        password += lock.timesThroughZero(command[0], int(command[1:]))
        
print(password)





            