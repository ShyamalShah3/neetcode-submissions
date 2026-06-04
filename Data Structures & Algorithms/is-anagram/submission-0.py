import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_count = (lambda: {letter: 0 for letter in string.ascii_lowercase})()
        t_count = (lambda: {letter: 0 for letter in string.ascii_lowercase})()
        for i in range(0, len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1
        return s_count == t_count
        