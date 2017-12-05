import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h1 = Hangman()

    # 기본 목숨은 6개 text = 7개, text-1 = 목숨
    def testDecreaseLife(self): # DecreaseLife에 대한 테스트
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)

    def testCurrentShape(self): #CurrentShape에 대한 테스트
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
'''
        )
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
'''
        )

if __name__ == '__main__':
    unittest.main()
