from ksuid import *
from utils import *
import unittest


class KSUIDTests(unittest.TestCase):

    def setUp(self):
        self.ksList = []
        for i in range(10000):
            self.ksList.append(ksuid())
            
        self.ksuid1 = ksuid()
        self.ksuid2 = ksuid()

    def testTimeStamp(self):
        self.assertTrue(self.ksuid1.getTimestamp() <=  self.ksuid2.getTimestamp())
        self.assertTrue(datetime.datetime.now().day == self.ksuid1.getDatetime().day)


    def testSort(self):
        self.assertTrue(len(self.ksList) > 0)
        ksList = sortKSUID(self.ksList)
        for index in range(len(ksList)-1):
            self.assertTrue(ksList[index].getTimestamp()  >= ksList[index+1].getTimestamp())



    def testStringFunction(self):
        for val in self.ksList:
            self.assertTrue(str(val) == str(val))
            


    def testDifferentUIDs(self):
        for val,index in enumerate(self.ksList):
            for val2, index2 in enumerate(self.ksList):
                if index == index2:
                    continue
                self.assertTrue(str(val2) != str(val))




if __name__ == "__main__":
    unittest.main()
