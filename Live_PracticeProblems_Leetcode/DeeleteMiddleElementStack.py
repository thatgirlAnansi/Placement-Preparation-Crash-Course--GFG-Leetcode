class Solution:
    
    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # Helper function for recursion
        def delete_middle(stack, size, current=0):
            # Base case: If we've reached the middle element, remove it
            if current == size // 2:
                stack.pop()
                return
            
            # Pop the current element
            top = stack.pop()
            
            # Recursive call to delete the middle element
            delete_middle(stack, size, current + 1)
            
            # Push the element back to the stack after the recursive call
            stack.append(top)

        # Call the recursive function to delete the middle element
        delete_middle(s, sizeOfStack)
