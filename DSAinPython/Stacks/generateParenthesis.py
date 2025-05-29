#Leetcode 22 - Given a pair of parenthesis, write a function to generate all combinations of well-formed parenthesis.
#Ex 1: i/p = 3, o/p = ["((()))", "(()())", "(())()", "()(())", "()()()"]
#Ex 2: i/p = 1, o/p = ["()"]

#The main logic to the program is
#   1. only add open parenthesis if open < n
#   2. only add a closing parenthesis if closed < open
#   3. valid if open == closed == n

class generateParenthesis:
    def genParent(self, num):

        stack = []
        result = []

        def backtrack(openN, closeN):
            if openN == closeN == num:
                result.append("".join(stack))
                return

            if openN < num:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN+1)
                stack.pop()

        backtrack(0,0)
        return result


obj = generateParenthesis()
array = obj.genParent(2)
print(f"The combinates are as follows : {array}")
