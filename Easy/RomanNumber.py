class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "O":0,
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        num = 0
        prev_sym = "O"
        for key in s:
            num = num + roman_dict.get(key)
            if roman_dict.get(prev_sym) < roman_dict.get(key):
                num = num - 2*roman_dict.get(prev_sym)
            prev_sym = key
        return num

sol = Solution()
print(sol.romanToInt('XXIV'))
