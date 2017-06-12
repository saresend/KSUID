from ksuid import *
from utils import *
import unittest


class KSUIDTests(unittest.TestCase):

    def setUp(self):
        self.ksList = []
        for i in range(10):
            self.ksList.append(KSUID())
            
        self.ksuid1 = KSUID()
        self.ksuid2 = KSUID()
        

    def testTimeStamp(self):
        self.assertTrue(self.ksuid1.getTimestamp() <=  self.ksuid2.getTimestamp())
        self.assertTrue(datetime.datetime.now().day == self.ksuid1.getDatetime().day)


        
    def testSort(self):

        self.assertTrue(len(self.ksList) > 0)
        print(sortKSUID(self.ksList))



    def testStringFunction(self):

        for val in self.ksList:
            self.assertTrue(val.toString() == val.toString())






if __name__ == "__main__":
    unittest.main()
