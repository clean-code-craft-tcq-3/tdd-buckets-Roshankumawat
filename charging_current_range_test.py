import unittest
import charging_current_range
class RangeBucketTest(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertTrue(Charging_current_range.binary_to_decimal("1111111111"==1023)
                        
    def test_range_details(self):
        self.assertTrue(charging_current_range.getRangeDetails([5, 5,6,7, 8, 1, 2, 2, 1, 1,2])==[(1 , 2 , 6), (5 , 8, 5)])
        self.assertTrue(charging_current_range.getRangeDetails([4, 5]) ==[(4 , 5 , 2)])
        self.assertTrue(charging_current_range.getRangeDetails([2, 3, 4, 6, 7]) == [(2 , 4 , 3), (6 , 7 , 2)])
   
if __name__ == '__main__':
    unittest.main()
