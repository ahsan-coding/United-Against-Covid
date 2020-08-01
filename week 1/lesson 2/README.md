# Lesson 2

## Conditional Statements (if, else and elif):

- If, else and elif are conditional statements that execute blocks of code according to a specific condition.
- Example:

```python
  if true:
    # do this code
  elif true:
    # do some different code
  else:
    # if all else fails do this code

```

## Operators:

- Definition - A character that represents an action (check, set/do set or do)
- Major operator types:
  - Assignment (set a variable equal to a value)
  - Arithmetic (add subtract multiply etc...)
  - Assignment [can fall under arithmetic] (add x amount to original variable)
  - Logical (or, and, or equal, and equal etc...)

### Arithmetic:

```python
sum = 1 + 1 # adds two numbers
subtract = 1 - 1 # subtracts two numbers
multiply = 1 * 2 # multiplies the two numbers
divide = 1 / 2 # divides the two numbers
modulus = 2 % 2 # returns the remainder after dividing the numbers
```

### Assignment:

```python
# (x represents any value)
variable = 1 # sets variable equal to x
variable += 1 # sets variable equal to x + 1
variable -= 1 # sets variable equal to x - 1
variable *= 1 # sets variable equal to x times 1
variable /= 1 # sets variable equal to x divided by 1
variable **= 1 # sets variable equal to x to the power of 1
```

### Comparison:

```python
x == 1 # returns true if x is equal to 1
x != 1 # returns true if x does not equal 1
x > 1 # returns true if x is greater than 1
x < 1 # returns true if x is less than 1
x >= 1 # returns true if x is greater than or equal to 1
x <= 1 # returns true if x is less than or equal to 1
```

### Logical:

```python
if x == 1 && x > 0:
  # checks if x equals one AND x is greater than 0
  # will run code if both statements are true

if x == 1 || x > 0:
  # checks if x equals one OR x is greater than 0
  # will run code if either statements are true
```

## Project:

- You have been asked to write a program for Sam’s Food Market. The program calculates the cost of grocery items from the store. It asks for the item and its price in cents. The program writes out the order and the charges. Regular shipping for items under $10 is $2.00; for items $10 or more shipping is $3.00. GST/HST tax in Ontario is 13% of the price.

```terminal
Item: Frozen Pizza
Price in coins: 450
Invoice:
  Price: $ 4.50
  Shipping: $ 2.00
  GST: $ 0.58
  Total: $ 7.08
```
