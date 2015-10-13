
import unittest
from MainPackage import somma


class Test(unittest.TestCase):

    def testName(self):
        self.assertEqual(somma(2,3),5,"La somma e sbagliata")

if __name__ == '__main__':
    unittest.main()