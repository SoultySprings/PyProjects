#Leetcode 20 - Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An i/p string is valid if
#   1. Open brackets must be closed by the same type of brackets
#   2. Open brackest must be closed byu the correct order
#As in s = "()" is True and s = "{)" is False

class validParenthesis:

    def invalid(self, str):
        stack = []
        Braces = {')':'(', ']':'[', '}':'{'}

        for char in str:
            if char in Braces:
                if stack and stack[-1] == Braces[char]:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(char)
        return True if not stack else False

text = '(){[]'
obj = validParenthesis()
print(f'The original text is : {text}.')
print(f'Resultant boolean is : {obj.invalid(text)}')
