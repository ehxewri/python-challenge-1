# Pseudocode for Taken a customer order in a food delivery truck

help
```
I was not challenged by the initial assignement
I wanted to come up with somehting that would requirement me to do more that just coding

All the elements of this assignment are in menu.py. 
```
```python
This program will have a menu defined with catagories and items in each catagory. 
some items have sub catagories but not all
Tasks:
Print main menu
Select catagory from main menu. store catagory as a string variable
Print item menu based on catagory
print a header
print each item with cost
if an item has sub items print the item - sub item together
Select item from sub menu
# Enter quantity for item selected
# Is the order complete? (y/n) Loop to main menu if yes
# Print items selected (item,price, qty,cost)
# Print Total at botttom of order list
# exit

```

We can plan our program by making observations about existing patterns, and writing rules to match.

Let's pseudocode the existing rules for our dishes.

```python
# Pattern recognition:
# 
# 
# 
```

Sometimes we have more information or content than is necessary for our process.

Let's add some pseudocode to remind us that there are details that are irrelevant to our solution:

```python
# Abstraction:
# Ignore non number input for menu/item selection
# Ignore non key seclection for menu/item selection
```

Oftentimes, there is a specific order that a process needs to be completed in. We can plan for this in pseudocode by writing out a sequence of events.

As we established in our kitchen cupboard, the fancy plates go on the top shelf and the plain plates and plain bowls go on the bottom shelf. In order to stack the plain bowls on top of the plain plates, putting away plates will have to come first in our sequence, followed by putting away bowls. If we begin to pseudocode this sequence, it could look something like the following:

```python
# Sequence:
while ording
# 1. Event 1: Select catagory
# 2. Event 2: Select item
# 3. Event 3: Enter qty

# 4. Event 5: Print items
#
# 5. Event 3: Print totals
```

Events can be further broken down into subtasks based on certain conditions.

In our dishes example, we have both fancy and plain plates that need to be sorted in different places. We need to add steps under the first event that will help us remember to sort the two. When we pseudocode this out, our new sequence might look something like the following:

```python
# Sequence:
# read key
# If key Value is dict get key2:value2
# concatinate Key " - " key2 
# set order-item [i]{"key" - "key2":value2}
# else
# set order-item[i]{"key":value}
```
Sometimes there are edge cases where we want to catch issues before they become a problem.

In our dishes example, what if we stumble across a plate that is chipped or broken? Let's adjust our conditional statement so that it includes additional conditions.

```python
# Sequence:
# 1. Event 1: input catagory
#    Conditional: If  catagory is (int)
#                   if catagory is key
#                       get item
#                       if item is (int)
#                           if item is key
#                                print (tbd)
# 
# #                 Else
#                    stack it on the bottom shelf
#    Debug: A fancy plate has a crack in it - what do we do?
#    Conditional: If (a plate is fancy)
#                    put it on the top shelf
#                 Else if (a plate is plain)
#                    put it on the bottom shelf
#                 Else if (a plate is cracked)
#                    put it in the trash
```

Another situation that commonly occurs is when we have to perform the same task a specified number of times.

In our dishes example, we have multiple bowls that all need to go in the same place. So, instead of a conditional, we can use a for loop.

```python
# Sequence:
# 2. Event 2: Put away bowls:
#    Loop: for (each bowl on the dish rack):
#                 stack it on the bottom shelf on top of the plain plates
```

Our final pseudocode for putting away dishes could look like this:

```python
# Algorithm: Put away clean dishes

# Tasks:
# Stack plain plates
# Stack fancy plates
# Stack plain bowls

# Pattern recognition:
# Plain plates go on the bottom shelf
# Fancy plates go on the top shelf
# Bowls go on the top of plain plates

# Abstraction:
# Ignore knife
# Ignore towel

# Sequence:
# 1. Event 1: Put away plates:
#    Conditional: If (a plate is fancy)
#                    stack it on the top shelf
#                 Else
#                    stack it on the bottom shelf
#    Debug: A fancy plate has a crack in it - what do we do?
#    Conditional: 
                Loop: for (each plate on the dish rack):
                    If (a plate is fancy)
#                    put it on the top shelf
#                   Else if (a plate is plain)
#                    put it on the bottom shelf
#                   Else if (a plate is cracked)
#                    put it in the trash
# 2. Event 2: Put away bowls:
#    Loop: for (each bowl on the dish rack):
#                 stack it on the bottom shelf on top of the plain plates
