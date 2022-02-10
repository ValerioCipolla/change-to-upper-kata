import unittest
from change_to_upper import change_to_upper

class Test(unittest.TestCase):
 def test1(self):
    self.assertEqual(change_to_upper(["apple", "banana"], 0), ["APPLE", "banana"])
    
 def test2(self):
   self.assertEqual(change_to_upper(["apple", "banana"], 1), ["apple", "BANANA"])

 def test3(self):
   self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry", "pear", "peach"], 5), ["apple", "banana", "strawberry", "berry", "pear", "PEACH"])

 def test4(self):
   self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry", "pear", "peach"], -1), ["APPLE", "BANANA", "STRAWBERRY", "BERRY", "PEAR", "PEACH"])

 def test5(self):
   self.assertEqual(change_to_upper(["apple", "banana", "strawberry", "berry"], 5), ["APPLE", "BANANA", "STRAWBERRY", "BERRY"])

 def test6(self):
   self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 3), ["mary", "valerio", "luis", "JONNY","rita"]) 

 def test7(self):
   self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 1) , ["mary", "VALERIO", "luis", "jonny", "rita"])

 def test8(self):
   self.assertEqual(change_to_upper(["mary", "valerio", "luis", "jonny", "rita"], 4) , ["mary", "valerio", "luis", "jonny", "RITA"])
 
 def test9(self):
   self.assertEqual(change_to_upper(["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"], 6) , ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "SATURDAY"])

 def test10(self):
  self.assertEqual(change_to_upper(["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"], 4) , ["sunday", "monday", "tuesday", "wednesday", "THURSDAY", "friday", "saturday"])

unittest.main()

