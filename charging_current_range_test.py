import unittest

class RangeBucketTest(unittest.TestCase):
    def test_range_details(self):
        # self.assertTrue(getRangeDetails([4, 5, 1, 2, 2, 1, 1,2])==8)
        self.assertTrue(getRangeDetails([4, 5]) == 2)
        self.assertTrue(getRangeDetails([2, 3, 4, 6, 7]) == 2)
        self.assertTrue(getRangeDetails([1, 5, 2, 3, 4]) == 5)
        self.assertTrue(getRangeDetails([4, 5,3,2,1,1,2,3])==8)

    
if __name__ == '__main__':
    unittest.main()
