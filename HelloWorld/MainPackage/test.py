
import unittest


class Test(unittest.TestCase):

    def testName(self):
        self.assertEqual(sum(2,3),5,"La somma e sbagliata")

if __name__ == '__main__':
    unittest.main()