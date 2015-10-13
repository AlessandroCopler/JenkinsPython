
import unittest


class Test(unittest.TestCase):


    def testName(self):
        self.assertEqual(sum(2,3),5,"Test riuscito")  


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()