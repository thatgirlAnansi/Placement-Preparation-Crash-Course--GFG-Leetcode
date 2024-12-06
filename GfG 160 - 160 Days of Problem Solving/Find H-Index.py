class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        citations.sort(reverse=True)
    
    # Step 2: Calculate H-Index
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:  # i + 1 is the 1-based index
                h = i + 1
            else:
                break
            
        return h
