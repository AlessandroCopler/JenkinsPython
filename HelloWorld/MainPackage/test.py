
import unittest
from Operazioni import Operazioni


class Test(unittest.TestCase):

    def testSomma(self):
        o=Operazioni(2,3)
        self.assertEqual(o.somma(),5,"La somma e sbagliata")

if __name__ == '__main__':
    unittest.main()