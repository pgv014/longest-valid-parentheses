# Longest Valid Parentheses

Python solution for the "Longest Valid Parentheses" problem.

## Algorithm

This solution uses a stack of indices.

- Push indices of '('.
- Pop when encountering ')'.
- Use a sentinel value (-1) to calculate valid lengths.
- Track the maximum valid substring length.

## Complexity

- Time: O(n)
- Space: O(n).
