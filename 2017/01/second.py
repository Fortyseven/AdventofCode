import math


def sumDigitsPt2(digits):
    sum = 0
    digits = str(digits)

    for i in range(len(digits)):
        if digits[i] == digits[(i+math.ceil(len(digits)/2)) % len(digits)]:
            sum += int(digits[i])
    return sum


# Example inputs
print("1212", sumDigitsPt2(1212))  # 6
print("1221", sumDigitsPt2(1221))  # 0
print("123425", sumDigitsPt2(123425))  # 4
print("123123", sumDigitsPt2(123123))  # 12
print("12131415", sumDigitsPt2(12131415))  # 4

# open input.txt read it in
with open('input.txt', 'r') as f:
    digits = f.read()
    print("input.txt", sumDigitsPt2(digits))
