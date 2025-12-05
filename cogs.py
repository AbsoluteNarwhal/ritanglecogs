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
            296,
            763,
            155, # guessed, q22
            145,
            168,
            437,
            733,
            154, 
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
        a = self.LEFT_COG[self.left_index]
        b = self.MIDDLE_COG[self.middle_index]
        c = self.RIGHT_COG[self.right_index]

        nums = sorted([a, b, c])
        x, y, z = nums[0], nums[1], nums[2]

        if x ** 2 + y ** 2 != z ** 2: return False

        if math.gcd(x, y) == 1 and math.gcd(y, z) == 1 and math.gcd(x, z) == 1: print(f"  Found pythagorean triple - a: {a}, b: {b}, c: {c}")
        return math.gcd(x, y) == 1 and math.gcd(y, z) == 1 and math.gcd(x, z) == 1
    
    def is60Triangle(self, tol=1e-3):
        a = self.LEFT_COG[self.left_index]
        b = self.MIDDLE_COG[self.middle_index]
        c = self.RIGHT_COG[self.right_index]

        if a + b <= c or a + c <= b or b + c <= a:
            return False

        def angle(opposite, side1, side2):
            cos_val = (side1**2 + side2**2 - opposite**2) / (2 * side1 * side2)
            cos_val = max(-1, min(1, cos_val))
            return math.degrees(math.acos(cos_val))

        A = angle(a, b, c)
        B = angle(b, a, c)
        C = angle(c, a, b)

        return abs(A - 60) < tol or abs(B - 60) < tol or abs(C - 60) < tol

    def isIntegerAreaTriangle(self):
        a = self.LEFT_COG[self.left_index]
        b = self.MIDDLE_COG[self.middle_index]
        c = self.RIGHT_COG[self.right_index]

        if a + b <= c or a + c <= b or b + c <= a:
            return False

        s = (a + b + c) / 2
        expr = s * (s - a) * (s - b) * (s - c)
        if expr < 0: return False

        area = math.sqrt(max(expr, 0))

        if abs(area - round(area)) < 1e-9:
            print(f"  Found integer area triangle - a: {a}, b: {b}, c: {c}")
            return True

        return False
    
    def goToNumber(self, x):
        while self.concatSelected() != x:
            self.tick()

    def test(self):
        num = self.concatSelected()
        p_counter = 0
        q_counter = 0
        r_counter = 0
        s_counter = 0

        print(f"testing fibonacci number: {num} at indexes left: {self.left_index}, middle: {self.middle_index}, right: {self.right_index}")

        while True:
            self.tick()
            p_counter += 1
            if self.isPythagoreanTriple(): 
                print(f"  p: {p_counter}")
                break

        while True:
            self.tick()
            q_counter += 1
            if self.is60Triangle(): 
                print(f"  q: {q_counter}")
                break

        while True:
            self.tick()
            r_counter += 1
            if self.isIntegerAreaTriangle(): 
                print(f"  r: {r_counter}")
                break

        while True:
            self.tick()
            s_counter += 1
            if isFibonacci(self.concatSelected()): 
                print(f"  s: {s_counter}")
                break

        print(f"  num: {num}, pqrs: {p_counter * q_counter * r_counter * s_counter}")
        return p_counter * q_counter * r_counter * s_counter

def main():
    lowest = 99999999999
    cogs = Cogs()
    for fibonacci in FIBONACCIS:
        cogs.goToNumber(fibonacci)
        lowest = min(lowest, cogs.test())
    print(lowest)

if __name__ == "__main__":
    main()