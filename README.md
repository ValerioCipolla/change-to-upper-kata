# change_to_upper KATA - ROOM 58

Thanks for checking out our kata. We created this to cement our Python skills (after only 5 hours of learning!).

To play please make sure you have a version of Python install on your machine by typing in your terminal

`python --version`

if you don't, make sure you [download](https://www.python.org/downloads/) it

## Play

To play clone the repo down, open the folder in your favourite code editor and open the `change_to_upper.py` file

Inside this file you will find instructions about the Kata, or you can read the instructions below.

Once you know what the kata is asking of you, fill the `change_to_upper` function inside the file with the code you think will solve the kata.

To see if your solution works run in your terminal:

`python change_to_upper_unittest.py`

No need to import the function into the testing file (we have already done it for you - make sure you don't change the name of the function)
If all tests pass you will see printed `OK` in your terminal, if not, you will see `FAILED`.

Keep trying until you have a working solution!

## Instructions

1. You are given a list called `array` and a number called `index`
2. You should return the list with the string at index `index` changed to upper case
3. If there is no element with that index in the list, you should return the list with all strings changed to upper case

### Examples:

- `change_to_upper(["apple", "banana"], 1)` should return `["apple", - - "BANANA"]`
- `change_to_upper(["apple", "banana"], 2)` should return `["APPLE", "BANANA"]`
- `change_to_upper(["apple", "banana"], -1)` should return `["APPLE", "BANANA"]`
