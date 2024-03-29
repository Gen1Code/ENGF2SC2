import random
import unittest
import re

class Set:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "Easy":
            self.size = 2
            self.A = {"A", "AB"}
            self.B = {"B", "AB"}
            self.C = {}
            self.Universe = self.A | self.B | {""}
        elif difficulty == "Medium" or difficulty == "Hard":
            self.size = 3
            self.A = {"A", "AB", "ABC", "AC"}
            self.B = {"B", "AB", "ABC", "BC"}
            self.C = {"C", "AC", "ABC", "BC"}
            self.Universe = self.A | self.B | self.C | {""}
        else:
            self.size = -1
            print("Not implemented")
        self.dic = {
            "UNION": "|",
            "AND": "&",
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

    def equationRegexCheck(self, text):
        pattern = r"([(-]*[ABC])+([\\&|^][(-]*[ABC][)]*)*"
        return bool(re.fullmatch(pattern, text))

    def regionRegexCheck(self,text):
        pattern = r"{(\'(?:A|B|C|AB|BC|AC|ABC){0,1}\',)*\'(?:A|B|C|AB|BC|AC|ABC){0,1}\'}"
        return bool(re.fullmatch(pattern,text))

    def generateRandomSetStatement(self):
        ## generate a random set statement
        operators = ['&', '|']
        min_rng = 0
        max_rng = 0
        if self.difficulty == "Medium":
            max_rng = 1
        if self.difficulty == "Hard":
            min_rng = 1
            max_rng = 2
            operators.append("\\")
            operators.append("^")

        st = ""
        for i in range(random.randint(min_rng, max_rng)):
            op = random.choice(operators)
            st += self.generateTwoSetStatement() + op
        st += self.generateTwoSetStatement()
        return st

    def generateTwoSetStatement(self):
        sets = ['A', 'B', "-A", "-B"]
        operators = ['&', '|']
        if self.size == 3:
            sets.append('C')
            sets.append("-C")
        if self.difficulty == "Hard":
            operators.append("\\")
            operators.append("^")
        statement = random.choice(sets)
        statement += random.choice(operators)
        statement += random.choice(sets)
        return statement

    def generateAndEvaluate(self):
        st = self.generateRandomSetStatement()
        ev = self.evaluate(st)
        return (st, ev)


class TestSet(unittest.TestCase):

    def test_set3(self):
        S = Set("Hard")
        self.assertEqual(S.evaluate("A Union B "), {"A", "AB", "B", "ABC", "AC", "BC"})
        self.assertEqual(S.evaluate("A And B "), {"AB", "ABC"})
        self.assertEqual(S.evaluate("A\B "), {"A", "AC"})
        self.assertEqual(S.evaluate("A\B And C "), {"AC"})
        self.assertEqual(S.evaluate("A ^ B "), {"A", "B", "AC", "BC"})
        self.assertEqual(S.evaluate("A ^ B ^ C "), {"A", "B", "C", "ABC"})


def main():
    S = Set("Hard")
    return S.generateAndEvaluate()


#print(main())
