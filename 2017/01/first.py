def sumDigits(digits):
    sum = 0
    digits = str(digits)
    for i in range(len(digits)):
        if digits[i] == digits[(i+1) % len(digits)]:
            sum += int(digits[i])
    return sum


# I had ChatGPT rewrite this function for me after I'd written
# my version. It works. But it's definitely a kick in the ass
# to learn more about how list comprehensions work.
#
# Also, I have to turn GitHub CoPilot off while doing these or
# it'll just dump the answers right in my lap. Great during regular
# work -- bad and unethical for puzzle contests like this.

def sumDigitsChatGPT(digits):
    digits = str(digits)
    return sum(int(digits[i]) for i in range(len(digits)) if digits[i] == digits[(i+1) % len(digits)])


# Example inputs
# print("1122", sumDigits(1122))
# print("1111", sumDigits(1111))
# print("1234", sumDigits(1234))
# print("91212129", sumDigits(91212129))


# open input.txt read it in
with open('input.txt', 'r') as f:
    digits = f.read()
    print(sumDigits(digits))
