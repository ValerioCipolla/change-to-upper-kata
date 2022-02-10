# you are given a list of strings and a number
# you should return the list with the string at index "number" in uppercase
# if there is no element in the list witn index "number" you should return the list with every element uppercase 

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