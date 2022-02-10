import unittest
from change_to_upper import change_to_upper

class TestSum(unittest.TestCase):
  def test_sum_with_1(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 0), ["APPLE", "banana"])
    
  def test_sum_with_2(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 1), ["apple", "BANANA"])

unittest.main()