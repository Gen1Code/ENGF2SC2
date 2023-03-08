import unittest


class Set:

    def __init__(self, size):
        if size == 2:
            self.A = {"A", "AB"}
            self.B = {"B", "AB"}
            self.C = {}
            self.Universe = self.A & self.B
        elif size == 3:
            self.A = {"A", "AB", "ABC", "AC"}
            self.B = {"B", "AB", "ABC", "BC"}
            self.C = {"C", "AC", "ABC", "BC"}
            self.Universe = self.A & self.B & self.C
        else:
            print("Not implemented")
        self.dic = {
            "Union": "|",
            "And": "&",
            " ^ ": "^",
            "-": "self.Universe -",
            " ": "",
            "/": "-",
            "A": "self.A",
            "B": "self.B",
            "C": "self.C"}
        return

    def replaceAll(self, text):
        for i, j in self.dic.items():
            text = text.replace(i, j)
        return text

    def evaluate(self, text):
        return eval(self.replaceAll(text))

    def __str__(self):
        return str(self.Universe)


class TestSet(unittest.TestCase):

    def test_set3(self):
        S = Set(3)
        self.assertEqual(S.evaluate("A Union B "),{"A", "AB", "B", "ABC", "AC", "BC"})
        self.assertEqual(S.evaluate("A And B "),{"AB", "ABC"})
        self.assertEqual(S.evaluate("A/B "),{"A", "AC"})
        self.assertEqual(S.evaluate("A/B And C "),{"AC"})
        self.assertEqual(S.evaluate("A ^ B "),{"A", "B", "AC", "BC"})
        self.assertEqual(S.evaluate("A ^ B ^ C "),{"A", "B", "C", "ABC"})

    def test_set2(self):
        S = Set(2)
        self.assertEqual(S.evaluate("A Union B "),{"A", "AB", "B"})
        self.assertEqual(S.evaluate("A And B "),{"AB"})
        self.assertEqual(S.evaluate("A/B "),{"A"})
        self.assertEqual(S.evaluate("A/B "),{"A"})
        self.assertEqual(S.evaluate("A ^ B "),{"A", "B"})
