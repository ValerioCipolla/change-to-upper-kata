import unittest
from change_to_upper import change_to_upper

class TestSum(unittest.TestCase):
  def test_sum_with_1(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 0), ["APPLE", "banana"])
    
  def test_sum_with_2(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 1), ["apple", "BANANA"])

  def test_sum_with_3(self):
    self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry", "pear", "peach"], 5), ["apple", "banana", "strawberry", "berry", "pear", "PEACH"])

  def test_sum_with_4(self):
    self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry", "pear", "peach"], -1), ["APPLE", "BANANA", "STRAWBERRY", "BERRY", "PEAR", "PEACH"])

  def test_sum_with_5(self):
    self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry"], 5), ["APPLE", "BANANA", "STRAWBERRY", "BERRY"])

  def test_sum_with_5(self):
    self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 3), ["mary", "valerio", "luis", "JONNY","rita"]) 

  

unittest.main()