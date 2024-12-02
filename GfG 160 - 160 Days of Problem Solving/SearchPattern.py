class Solution:
    def search(self, pat, txt):
        result = []
        for i in range(len(txt) - len(pat) + 1):
            if txt[i:i + len(pat)] == pat:
                result.append(i)
        return result
