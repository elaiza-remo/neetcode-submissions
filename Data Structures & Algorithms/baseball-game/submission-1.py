class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ''' 
        Go through each part of the operations, add the results to a stack
        ''' 
        for item in operations:
            if item == '+':
                # Add the result to the end of the stack\
                stack.append(stack[-1] + stack[-2])
            elif item == "D":
                # Grab the last value in the stack and double it
                stack.append(stack[-1] * 2)
            elif item == "C":
                # Grab the previous score and remove it
                stack.pop()
            else:
                # The item is an integer, just convert to int and then append it in
                num = int(item)
                stack.append(num)
        # Now sum the whole list up
        return sum(stack)