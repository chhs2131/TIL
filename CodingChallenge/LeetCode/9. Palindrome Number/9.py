# Palindrome: 앞으로 읽어도 뒤로 읽어도 같은 문장

class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math

        if x < 0:
            return False

        xxx = x
        while xxx != 0:
            print("now xxx:", xxx)
            last = xxx % 10
            first_digit = 10 ** int(math.log10(xxx))
            first = int(xxx / first_digit)

            print(last, "==", first)
            if first == last:
                xxx -= first * first_digit
                xxx = int(x / 10)
            else:
                return False
        return True
