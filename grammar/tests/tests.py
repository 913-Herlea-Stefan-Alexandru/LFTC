from grammar.domain.Grammar import Grammar
from grammar.domain.Parser import Parser
import unittest


class DemoTest(unittest.TestCase):
    def test_grammar_parser(self):
        gr = Grammar("../res/g5.txt")
        assert gr.cfg_check()

        pr = Parser(gr)
        first = pr.first()
        follow = pr.follow()
        first_res = {'S': ['a'], 'A': ['a'], 'C': ['c'], 'B': ['b', 'r'], "A'": ['d', 'eps'], "A''": ['c', 'b', 'r']}
        follow_res = {'S': ['$'], 'A': ['k'], 'C': ['d', 'k'], 'B': ['d', 'k'], "A'": ['k'], "A''": ['k']}
        for key in first:
            self.assertCountEqual(first[key], first_res[key])
            self.assertCountEqual(follow[key], follow_res[key])

    def test_grammar_parser2(self):
        gr = Grammar("../res/g4.txt")
        assert gr.cfg_check()

        pr = Parser(gr)
        first = pr.first()
        follow = pr.follow()
        first_res = {'E': ['id', '('], "E'": ['+', 'eps'], 'T': ['id', '('], "T'": ['eps', '*'], 'F': ['id', '(']}
        follow_res = {'E': ['$', ')'], "E'": ['$', ')'], 'T': ['$', ')', '+'], "T'": ['$', ')', '+'], 'F': ['$', ')', '+', '*']}
        for key in first:
            self.assertCountEqual(first[key], first_res[key])
            self.assertCountEqual(follow[key], follow_res[key])


if __name__ == '__main__':
    unittest.main()
