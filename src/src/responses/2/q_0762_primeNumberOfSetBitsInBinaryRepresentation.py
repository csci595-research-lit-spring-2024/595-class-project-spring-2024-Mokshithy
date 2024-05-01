class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        count = 0
        for num in range(left, right + 1):
            bits = bin(num).count('1')
            if is_prime(bits):
                count += 1
                
        return count