class Solution:
   def romanToInt(self, s):

        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,'D': 500, 'M': 1000 }
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

if __name__ == "__main__":
    sol = Solution()
    test_cases = ["III", "LVIII", "MCMXCIV"]
    for roman in test_cases:
        a = sol.romanToInt(roman)
        print(roman,"=", a )
