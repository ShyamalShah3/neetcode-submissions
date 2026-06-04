import string
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters = defaultdict(lambda: 0)
        t_letters = defaultdict(lambda: 0)

        for i in range(len(s)):
            s_letters[s[i]] += 1
            t_letters[t[i]] += 1
        
        return s_letters == t_letters
        
        