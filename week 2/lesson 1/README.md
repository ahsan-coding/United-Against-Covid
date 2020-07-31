# Lesson 1 Arrays and Dictionaries

## Introduction to arrays:

Arrays are a datatype that allow users to store information in a certain location within said data. Example `[1, 2, 3]`
Some arrays are _mutable_ (can be changed) and some are _immutable_ (can't be changed)

```python
 Array   [1, 2, 3]
          |  |  |
 Location 0  1  2

 # to access the information
 myArray = [1, 2, 3]
 print(myArray[0])
 # expected output 1
```

### Types of arrays:

- Lists: a type of mutable array that can have duplicates. **Syntax:** `[]`
- Tuples: a type of immutable array that can have duplicates. **Syntax:** `()`
- Sets: a type of immutable array that can't have duplicates. **Syntax:** `{}`

**SEE `arrayTypes.py` FOR MORE DETAILS**

## Introduction to Dictionaries:

Similar to how arrays have locations for information within itself and use said locations to access the information. Dictionaries have _keys_ (some string that acts as an identifier for data) which are used to access information

- Dictionaries are mutable and can have repeating data

**Syntax:**

```python
someDictionary = {
  "keyName": "someInformation"
}
# access the item with said key
print(someDictionary["keyName"])

# update information in dictionary
someDictionary["keyName"] = True

# remove information from dictionary
delete someDictionary["keyName"]

# remove dictionary completely
delete someDictionary
```

## Project:

- Create a dictionary that has the age for 5 people named (Jim, Jack, Terry, Sam and Bob)
- Create a set of 5 prime numbers
- Create a tuple of 3 special numbers
- Ask the user for 10 numerical inputs and store these inputs in a list
- Cross reference the list with each of the items above and output any matches

Example output:

```
User input 1: 8
User input 2: 56
User input 3: 7
User input 4: 11
User input 5: 99
User input 6: 210521
User input 7: 9
User input 8: 55
User input 9: 25
User input 10: 1

User input 2 is the same as Bob's age
User input 3 is a prime number
User input 4 is a prime number
User input 9 is a special number
User input 10 is a special number

```
