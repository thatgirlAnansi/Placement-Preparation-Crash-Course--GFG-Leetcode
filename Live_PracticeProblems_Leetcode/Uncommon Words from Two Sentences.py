class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        word_count = Counter(words)
    
    # Find words that appear exactly once
        uncommon = [word for word in word_count if word_count[word] == 1]
    
        return uncommon  
