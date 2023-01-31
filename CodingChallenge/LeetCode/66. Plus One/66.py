class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = self.toNumber(digits)
        return self.toDigits(number + 1)

    def toNumber(self, digits):
        string = ""
        for digit in digits:
            string += str(digit)
        return int(string)

    def toDigits(self, number):
        digits = []
        number = list(str(number))
        for n in number:
            digits.append(int(n))
        return digits
