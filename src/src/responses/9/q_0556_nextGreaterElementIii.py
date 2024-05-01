class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = len(digits) - 1
        while j > i and digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        result = int(''.join(digits[:i + 1] + digits[i + 1:][::-1]))
        return result if result <= 2**31 - 1 else -1
