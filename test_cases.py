import unittest
from re_test import rearranage_name

class arrange_test(unittest.TestCase):
    def test1(self):
        testcase = 'mobayyed, motasem'
        expected = 'motasem, mobayyed'
        self.assertEqual(rearranage_name(testcase), expected)
    
    def test2(self):
        testcase = 'motkasem, mobayyed'
        expected = 'mobayyed, motasem'
        self.assertEqual(rearranage_name(testcase), expected)

    def test3(self):
        testcase = 'hello motasem'
        expected = 'hello motasem'
        self.assertEqual(rearranage_name(testcase), expected)

unittest.main()

