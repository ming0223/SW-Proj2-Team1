import unittest

from word import Word

class TestWord(unittest.TestCase):

    def setUp(self):
        self.word = Word('words.txt')

    def testRandFromDB(self):
        self.assertIn(self.word.randFromDB(), self.word.words)


if __name__ == '__main__':
    unittest.main()
