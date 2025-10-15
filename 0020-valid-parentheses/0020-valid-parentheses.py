class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in pairs.values():      # Opening bracket
                stack.append(ch)
            elif ch in pairs:             # Closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                return False               # Invalid character (shouldn't happen)
        
        return not stack


#  Test locally
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["()", "()[]{}", "(]", "([])", "([)]"]
    for s in test_cases:
        print(s, sol.isValid(s))
