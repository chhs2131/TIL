class Solution:
    import re

    def lengthOfLastWord(self, s: str) -> int:
        tokens = re.findall('\w+', s)
        return len(tokens[-1])
