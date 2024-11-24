class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        # Length of each substring
        n = len(s)
        len_sub = n // k
        
        # Split both strings into k substrings of length len_sub
        s_substrings = [s[i:i+len_sub] for i in range(0, n, len_sub)]
        t_substrings = [t[i:i+len_sub] for i in range(0, n, len_sub)]
        
        # Use a hashmap (Counter) to count occurrences of substrings
        s_count = Counter(s_substrings)
        t_count = Counter(t_substrings)
        
        # Compare the frequency maps of substrings
        return s_count == t_count
