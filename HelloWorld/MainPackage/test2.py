import unittest
from Operazioni import Operazioni


class Test(unittest.TestCase):


    def testDifferenzaNegativa(self):
        o=Operazioni(2,3)
        self.assertEqual(o.differenza(),-1,"La differenza non e nulla")
    
    def testDifferenzaPositiva(self):
        o=Operazioni(3,2)
        self.assertEqual(o.differenza(),1,"La differenza non sono riuscito a farla")

if __name__ == "__main__":
    unittest.main()