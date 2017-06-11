from ksuid import KSUID
import unittest


class KSUIDTests(unittest.TestCase):

    def setUp(self):
        self.ksuid1 = KSUID()
        self.ksuid2 = KSUID()
        

    def testTimeStamp(self):
        self.assertTrue(self.ksuid1.getTimeStamp() <=  self.ksuid2.getTimeStamp())










if __name__ == "__main__":
    unittest.main()
