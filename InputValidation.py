import unittest


class InputValidation:
    def __init__(self, input):
        self.input = input

    def balancedParentheses(self):
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        stack = []
        str = self.input
        for i in str:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                    stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


    def onlyValidChars(self):
        allowed = ['A','B','C','-C','-B','-A']



class TestInputValidation(unittest.TestCase):
    def test_balancedParentheses(self):
        self.assertTrue(InputValidation("()").balancedParentheses())
        self.assertTrue(InputValidation("()[]{}").balancedParentheses())
        self.assertFalse(InputValidation("([)]").balancedParentheses())
        self.assertFalse(InputValidation("([)]").balancedParentheses())
