import math

def isPerfectSq(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(x):
    return isPerfectSq(5 * x * x + 4) or isPerfectSq(5 * x * x - 4)
    
class Cogs:
    def __init__(self):
        self.left_index = 0
        self.middle_index = 0
        self.right_index = 0

        self.LEFT_COG = [
            267,
            851,
            259,
            433,
            493,
            165,
            701,
            102
        ]

        self.MIDDLE_COG = [
            914,
            494,
            468,
            460,
            143,
            150,
            832,
            580,
            299,
            334,
            408
        ]

        self.RIGHT_COG = [
            296,
            # q21
            # q22
            145,
            # q24
            # q25
            733,
            # q27
            # q28
        ]

    def tick(self):
        self.left_index += 1
        self.middle_index += 1
        self.right_index += 1

        if self.left_index >= len(self.LEFT_COG):
            self.left_index = 0

        if self.middle_index >= len(self.MIDDLE_COG):
            self.middle_index = 0

        if self.right_index >= len(self.RIGHT_COG):
            self.right_index = 0

    def getSelected(self):
        return int(str(self.LEFT_COG[self.left_index]) + str(self.MIDDLE_COG[self.middle_index]) + str(self.RIGHT_COG[self.right_index]))

    def getClicker(self):
        return self.LEFT_COG[(self.left_index + 2) % 8]

def main():
    pass

if __name__ == "__main__":
    main()