import unittest
import charging_current_range


class RangeBucketTest(unittest.TestCase):
    def test_range_details(self):
        self.assertTrue(charging_current_range. checkRange([4, 5]) == (4,5,1))
        self.assertTrue(charging_current_range. checkRange([2, 3, 4,5, 6, 7]) == (2,7,6))
        self.assertTrue(charging_current_range. checkRange([1, 5, 2, 3, 4]) == (1,5, 5))

    
if __name__ == '__main__':
    unittest.main()
