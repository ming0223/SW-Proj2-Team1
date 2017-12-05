import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.secretWord, 'default')
        self.assertEqual(self.g1.currentStatus, '_e____')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.guess('d'), True) #단어에 있는 글자가 들어갔을 때 Guess 리턴 값
        self.g1.guess('f')
        self.assertEqual(self.g1.guess('j'), False) #단어에 없는 글자가 들어갔을 때 리턴 값
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testFinished(self):
        self.g1.guess('d')
        self.g1.guess('e')
        self.g1.guess('f')
        self.assertNotEqual(self.g1.finished(), True) #finished함수가 secretWord를 완성시키지 않았을 때 종료하지 않는지
        self.g1.guess('a')
        self.g1.guess('u')
        self.g1.guess('l')
        self.g1.guess('t')
        self.assertEqual(self.g1.finished(), True) #종료가 잘 되는지

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('u') #전에 입력되었던 값이 입력되었을 때
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('U') #대문자가 입력이 되었을때
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')


if __name__ == '__main__':
    unittest.main()
