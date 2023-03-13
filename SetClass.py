import random
import unittest
import re

class Set:

    def __init__(self, size):
        if size == 2:
            self.size = 2
            self.A = {"A", "AB"}
            self.B = {"B", "AB"}
            self.C = {}
            self.Universe = self.A | self.B | {""}
        elif size == 3:
            self.size = 3
            self.A = {"A", "AB", "ABC", "AC"}
            self.B = {"B", "AB", "ABC", "BC"}
            self.C = {"C", "AC", "ABC", "BC"}
            self.Universe = self.A | self.B | self.C | {""}
        else:
            self.size = -1
            print("Not implemented")
        self.dic = {
            "Union": "|",
            "And": "&",
            " ^ ": "^",
            "-": "self.Universe -",
            " ": "",
            "\\": "-",
            "A": "self.A",
            "B": "self.B",
            "C": "self.C"
        }

    def replaceAll(self, text):
        for i, j in self.dic.items():
            text = text.replace(i, j)
        return text

    def evaluate(self, text):
        return eval(self.replaceAll(text))

    def balancedParentheses(self, text):
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        stack = []
        for i in text:
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

    def regexCheck(self, text):
        # Check if text is a valid set statement
        pattern = r'^([ABC]*|[ABC]*\\[ABC]*|[ABC]*&[ABC]*|[ABC]*\|[ABC]*|[ABC]*\^[ABC]*)$'
        if re.match(pattern, text):
            return True
        else:
            return False

    def generateRandomSetStatement(self):
        ## generate a random set statement

        operators = ['\\', '&', '|','^']
        st = ""
        for i in range(0):
            op = random.choice(operators)
            st += self.generateTwoSetStatement() + op
        st += self.generateTwoSetStatement()
        return st

    def generateTwoSetStatement(self):
        sets = ['A', 'B',"-A","-B"]
        operators = ['\\', '&', '|', '^']
        if self.size == 3:
            sets.append('C')
            sets.append("-C")
        statement = random.choice(sets)
        statement += random.choice(operators)
        statement += random.choice(sets)
        return statement


class TestSet(unittest.TestCase):

    def test_set3(self):
        S = Set(3)
        self.assertEqual(S.evaluate("A Union B "), {"A", "AB", "B", "ABC", "AC", "BC"})
        self.assertEqual(S.evaluate("A And B "), {"AB", "ABC"})
        self.assertEqual(S.evaluate("A\B "), {"A", "AC"})
        self.assertEqual(S.evaluate("A\B And C "), {"AC"})
        self.assertEqual(S.evaluate("A ^ B "), {"A", "B", "AC", "BC"})
        self.assertEqual(S.evaluate("A ^ B ^ C "), {"A", "B", "C", "ABC"})

    def test_set2(self):
        S = Set(2)
        self.assertEqual(S.evaluate("A Union B "), {"A", "AB", "B"})
        self.assertEqual(S.evaluate("A And B "), {"AB"})
        self.assertEqual(S.evaluate("A\B "), {"A"})
        self.assertEqual(S.evaluate("A\B "), {"A"})
        self.assertEqual(S.evaluate("A ^ B "), {"A", "B"})


def main():
    S = Set(3)
    st = S.generateRandomSetStatement()
    print(st)
    print(S.replaceAll(st))
    return S.evaluate(st)


#print(main())
