import unittest
import charging_current_range
import Current_sensing_at_high_fidility

class RangeBucketTest(unittest.TestCase):
   
    def test_range_details(self):
        self.assertTrue(charging_current_range.getRangeDetails([5, 5,6,7, 8, 1, 2, 2, 1, 1,2])==[(1 , 2 , 6), (5 , 8, 5)])
        self.assertTrue(charging_current_range.getRangeDetails([4, 5]) ==[(4 , 5 , 2)])
        self.assertTrue(charging_current_range.getRangeDetails([2, 3, 4, 6, 7]) == [(2 , 4 , 3), (6 , 7 , 2)])
        
    def test_sensor_output(self):
        self.assertTrue(Current_sensing_at_high_fidility.decimal_to_binary(123)==(['0','0','0', '0', '0', '1', '1', '1', '1', '0', '1', '1']))
        self.assertFalse(Current_sensing_at_high_fidility.decimal_to_binary(1324)==(['0','0','0', '0', '0', '1', '1', '1', '1', '0', '1', '1']))
        self.assertTrue(Current_sensing_at_high_fidility.current_from_sensor(['0','0','0', '0', '0', '1', '1', '1', '1', '0', '1', '1'])==0)
        self.assertTrue(Current_sensing_at_high_fidility.current_from_sensor(Current_sensing_at_high_fidility.decimal_to_binary(1234))==3)
if __name__ == '__main__':
    unittest.main()
