# Nested Conditional Statement
A conditional statement inside another conditional statement.

## Indentation
The header / clause of a nested conditional statement must be indented from an outter header.

## Formula
```python
if (CONDITION):
  BODY STATEMENT
  
  if (CONDITION):     <--- Starting a nested conditional statement
    BODY STATEMENT

  elif (CONDITION):
    BODY STATEMENT

  else:
    BODY STATEMENT    <--- Ending a nested conditional statement

elif (CONDITION):
  BODY STATEMENT
  
else:
  BODY STATEMENT

```
Ex.
```python
x = 10
y = 10

if (x < y): # False
  print ("x is less than y")
else:
  if (x > y): # False
    print ("x is greater than y")
  else:
    print ("x and y must be equal")
```
> x and y must be equal