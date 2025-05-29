import stack

class linter:
    def __init__(self):
        self.stack = stack.stack()

    # def lint(self, text):
    #     while self.stack.read():
    #         self.stack.pop()
    #
    #     matching_braces = {"(": ")", "[": "]", "{": "}"}
    #     for char in text:
    #         if char in matching_braces.keys():
    #             self.stack.push(char)
    #         elif char in matching_braces.values():
    #             if not self.stack.read():
    #                 return char + " does not have opening brace"
    #         else:
    #             popped_opening_brace = self.stack.pop()
    #             if char != matching_braces.get(popped_opening_brace):
    #                 return char + " has mismatched opening brace"
    #         # If we get to the end of line, and the stack isn't empty:
    #     if self.stack.read():
    #         return self.stack.read() + " does not have closing brace"
    #         return True

    def lint(self, text):
        print(text)
        while self.stack.read():
            self.stack.pop()

        matchingBraces = {'(':')', '{':'}', '[':']'}
        for char in text:
            print(char, end="\t\t")
            if char in matchingBraces.keys():
                self.stack.push(char)
            elif char in matchingBraces.values():
                if not self.stack.read():
                    return char + ' does not have opening braces'
            else:
                poppedOpeningBrace = self.stack.pop()
                if char != matchingBraces.get(poppedOpeningBrace):
                    return char + ' has mismatched opening brace'
            print(self.stack.read())

        if self.stack.read():
            return self.stack.read() + ' does not have closing brace'
        return True

if __name__ == '__main__':
    text = '(this has {[figure it out]})'
    print(f'Original text : \'{text}\'')
    obj = linter()
    print(obj.lint(text))

