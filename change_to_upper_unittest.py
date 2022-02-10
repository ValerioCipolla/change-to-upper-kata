import unittest
from change_to_upper import change_to_upper

class TestChangeTOUpper(unittest.TestCase):
  def change_to_upper_1(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 0), ["APPLE", "banana"])
    
  def change_to_upper_2(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 1), ["apple", "BANANA"])

  def change_to_upper_3(self):
    self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry", "pear", "peach"], 5), ["apple", "banana", "strawberry", "berry", "pear", "PEACH"])

  def change_to_upper_4(self):
    self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry", "pear", "peach"], -1), ["APPLE", "BANANA", "STRAWBERRY", "BERRY", "PEAR", "PEACH"])

  def change_to_upper_5(self):
    self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry"], 5), ["APPLE", "BANANA", "STRAWBERRY", "BERRY"])

  def change_to_upper_6(self):
    self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 3), ["mary", "valerio", "luis", "JONNY","rita"]) 

def change_to_upper_7(self):
  self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 1) , ["mary", "VALERIO", "luis", "jonny", "rita"])

def change_to_upper_8(self):
  self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 4) , ["mary", "VALERIO", "luis", "jonny", "RITA"])
  

def change_to_upper_9(self):
  self.assertEqual(change_to_upper(["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"], 6) , ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "SATURDAY"])

def change_to_upper_10(self):
  self.assertEqual(change_to_upper(["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"], 4) , ["sunday", "monday", "tuesday", "wednesday", "THURSDAY", "friday", "saturday"])
unittest.main()