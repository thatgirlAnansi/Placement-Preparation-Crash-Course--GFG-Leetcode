        n = len(arr)
        
        # Step 1: Segregate positive and non-positive numbers
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        # Only work with the positive part of the array
        positive_part = arr[j:]
        size = len(positive_part)
        
        # Step 2: Mark presence of numbers
        for i in range(size):
            num = abs(positive_part[i])
            if 1 <= num <= size:
                if positive_part[num - 1] > 0:
                    positive_part[num - 1] = -positive_part[num - 1]
        
        # Step 3: Find the first missing positive number
        for i in range(size):
            if positive_part[i] > 0:
                return i + 1
        
        # If all indices are marked, the missing number is size + 1
        return size + 1
