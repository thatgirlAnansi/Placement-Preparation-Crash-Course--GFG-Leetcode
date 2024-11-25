class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	    max_product = arr[0]
        min_product = arr[0]
        result = arr[0]

        # Iterate through the array starting from the second element
        for num in arr[1:]:
            # Swap max_product and min_product if the current number is negative
            if num < 0:
                max_product, min_product = min_product, max_product

            # Update max_product and min_product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Update the result with the maximum product so far
            result = max(result, max_product)
        
        return result
