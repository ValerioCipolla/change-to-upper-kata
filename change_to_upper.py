# You are given a list called array and a number called index
# You should return the list with the string at index "index" changed to upper case
# If there is no element with that index in the list, you should return the list with all strings changed to upper case
# Examples:
# change_to_upper(["apple", "banana"], 1)` should return `["apple", "BANANA"]
# change_to_upper(["apple", "banana"], 2)` should return `["APPLE", "BANANA"]
# change_to_upper(["apple", "banana"], -1)` should return `["APPLE", "BANANA"]

def change_to_upper(array, index):
  if index >= len(array):
    newList = []
    for x in array:
      newList.append(x.upper())
    return newList
  elif index < 0:
    newList = []
    for x in array:
      newList.append(x.upper())
    return newList
  else:
    array[index] = array[index].upper()
    return array