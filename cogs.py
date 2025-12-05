import math

def isPerfectSq(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(x):
    return isPerfectSq(5 * x * x + 4) or isPerfectSq(5 * x * x - 4)

FIBONACCIS = [
    102334155,
    165580141,
    267914296,
    433494437,
    701408733
]
    
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
            # still need 155 and 733
            296,
            0, # q21
            0, # q22
            145,
            168,
            437,
            733,
            0, # q27
            141
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

    def concatSelected(self):
        return int(str(self.LEFT_COG[self.left_index]) + str(self.MIDDLE_COG[self.middle_index]) + str(self.RIGHT_COG[self.right_index]))

    def getClicker(self):
        return self.LEFT_COG[(self.left_index + 2) % 8]
    
    def isPythagoreanTriple(self):
        nums = sorted([self.LEFT_COG[self.left_index], self.MIDDLE_COG[self.middle_index], self.RIGHT_COG[self.right_index]])
        x, y, z = nums[0], nums[1], nums[2]

        if x ** 2 + y ** 2 != z ** 2: return False
        return math.gcd(x, y) == 1 and math.gcd(y, z) == 1 and math.gcd(x, z) == 1
    
    def is60Triangle(self):
        a = self.LEFT_COG[self.left_index]
        b = self.MIDDLE_COG[self.middle_index]
        c = self.RIGHT_COG[self.right_index]

        angle_A = math.degrees(math.asin((a**2 - b**2 - c**2) / (-2) * b * c))
        angle_B = math.degrees(math.asin((b**2 - a**2 - c**2) / (-2) * a * c))
        angle_C = math.degrees(math.asin((c**2 - a**2 - b**2) / (-2) * a * b))

        return angle_A == 60 or angle_B == 60 or angle_C == 60

    def isIntegerAreaTriangle(self):
        semi = (self.LEFT_COG[self.left_index] + self.MIDDLE_COG[self.middle_index] + self.RIGHT_COG[self.right_index]) / 2
        area = math.sqrt(semi * (semi - self.LEFT_COG[self.left_index]) * (semi - self.MIDDLE_COG[self.middle_index]) * (semi - self.RIGHT_COG[self.right_index]))
        return int(area) == area
    
    def goToNumber(self, x):
        while self.concatSelected() != x:
            self.tick()

    def test(self):
        num = self.concatSelected()
        p_counter = 0
        q_counter = 0
        r_counter = 0
        s_counter = 0

        while True:
            self.tick()
            p_counter += 1
            if self.isPythagoreanTriple(): break

        while True:
            self.tick()
            q_counter += 1
            if self.is60Triangle(): break

        while True:
            self.tick()
            r_counter += 1
            if self.isIntegerAreaTriangle(): break

        while True:
            self.tick()
            p_counter += 1
            if isFibonacci(self.concatSelected()): break

        print(f"num: {num}, pqrs: {p_counter * q_counter * r_counter * s_counter}")
        return p_counter * q_counter * r_counter * s_counter

def main():
    lowest = 99999999999
    cogs = Cogs()
    for fibonacci in FIBONACCIS:
        cogs.goToNumber(fibonacci)
        lowest = min(lowest, cogs.test())

if __name__ == "__main__":
    main()