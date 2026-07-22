class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "(()",
        ")()())",
        "",
        "()(()",
        "()(())",
        "(()())"
    ]

    for s in test_cases:
        print(f"Input: {s!r}")
        print(f"Output: {solution.longestValidParentheses(s)}")
        print("-" * 30)
        