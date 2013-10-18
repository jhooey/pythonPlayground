#whitespace in Python is significant
 
#This is a single line comment
"""This
		is
			a
			   multiline 
					comment"""
#####################################ASSIGNMENTS##################################
#You can assign multiple values in a single line
number1, number2, string1 = 1, 2 , "string"

#The common problem of switching variable values without using a third variable
#this works because the values are placed into the right hand side then the assignment is completed 
a,b = 1,2 
a, b = b, a
print a,b
#####################################Date and Time################################
from datetime import datetime

now = datetime.now()
print now
month 	= now.month
day 	= now.day
year	= now.year
hour	= now.hour
minute	= now.minute
second	= now.second
print str(month) + "/" + str(day) + "/" + str(year) + " " + str(hour) + ":" + str(minute) +":"+ str(second)

########################################STRINGS####################################
print ('STRING OUTPUTS')
#convert to string
number = 23
str(number)

"""string = number + string == Error
		you must convert everything before concatenating the string"""
#\ is an escape character
string = 'I\'m still a string'

#you can choose a character because strings are indexed like arrays
"""
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5
  """
fifth_letter = "MONTY"[4]
print fifth_letter
fifth_letter = "MONTY"[-1]#you can also start from the end of the string
print fifth_letter
substring = "MONTY"[1:-1]#you can also select a substring
print substring
substring = "MONTY"[1:] #select a substring from index 1 to the end of the string
print substring

#Get the length of a string
print len(substring)
#Convert string to all lowercase
print substring.lower()
#Convert string to all uppercase
print substring.upper()

# The % string formatter replaced the %s (the "s" is for "string") in our string with the variables in parentheses.
string_1 = "Camelot"
string_2 = "place"
string_3 = "Let's not go to %s. 'Tis a silly %s."
string_4 = "Holland"
string_5 = "place"
print string_3 % (string_1, string_2)
print string_3 % (string_4, string_5)

######################################LISTS###############################################################
zoo_animals = ["pangolin", "cassowary", "sloth", "platypus" ];
# You can access an individual item on the list by its index
#List indices begin with 0, not 1! 
print "The first animal at the zoo is the " + zoo_animals[0]
print "The second animal at the zoo is the " + zoo_animals[1]
print "The third animal at the zoo is the " + zoo_animals[2]
print "The fourth animal at the zoo is the " + zoo_animals[3]

#A list index behaves like any other variable name! It can be used to access as well as assign values.
zoo_animals[2] = "hyena"
#In Python, we say lists are mutable: that is, they can be changed.
zoo_animals.append("bear")


"""
list_name[a:b] will return a portion of list_name starting with the index a and ending before the index b.
"""
my_list = [0, 1, 2, 3]
my_slice = my_list[1:3]
print my_slice

"""
.index(VALUE)
You can search through a list with the index() function. 
my_list.index("dog") will return the first index that contains the string "dog"

.insert(INDEX,VALUE)
Items can be added to the middle of a list (instead of to the end) with the insert() function. 
my_list.insert(4,"cat") adds the item "cat" at index 4 of my_list, and moves the item previously at index 4 and 
all items following it to the next index (that is, they all get bumped towards the end by one).

.sort()
If your list is a jumbled mess, you may need to sort() it. 
my_list.sort() will sort the items in my_list in increasing numerical/alphabetical order.

It's worth noting that sort() does not return a new list; 
instead, your existing my_list is sorted in place (the sorted version replaces the unsorted version).

.remove(VALUE)
Lists have a method called .remove(VALUE) which will remove the first instance of the value passed to it.
"""


######################################DICTIONARIES###########################################################
"""
A dictionary is similar to a list, but you access values by looking up a key instead of an index. 

1. A single dictionary can hold many types of values. The inventory dict here has both int and list values.

2. A dictionary's keys MUST be both immutable and hashable. Don't worry if you don't understand what that means. 
    In general, we only use strings, numbers or tuples as keys, but not lists, dictionaries or sets. 
    The values can be anything you'd like.

3. When you access a value in a dictionary you have access to that value directly.

A key can be any string or number. Dictionaries are enclosed in curly braces, like so:
"""
d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

d['key4'] = 4

#Items can be removed from a dictionary with the del command:
del d['key2']

#A new value can be associated with a key by assigning a value to the key, like so:
d['key3'] = 42


#############################################FOR LOOP########################################################

my_list = [1,9,3,8,5,7]
#A variable name follows the for keyword; it will be assigned the value of each list item in turn
for number in my_list:
    print 2*number
    
######################################Booleans################################################################
""" True
	False
	must be capitalized
	"""
#Boolean Operators
"""
==	!=	>=	<=	<	>
and 	or		not
order of precedence or order of operations for boolean operators. The order is as follows:
not is evaluated first;
and is evaluated next;
or is evaluated last.
"""

###########################################CONDITIONAL STATEMENTS############################################
"""
if EXPRESSION:
    # block line one
    # block line two
    # et cetera
elif EXPRESSION: 
    # block line one
    # block line two
    # et cetera
else:
    # block line one
    # block line two
    # et cetera
"""
#############################################FUNCTIONS#######################################################

def function_name(parameters):
    """docstring, which is a triple-quoted, multi-line comment that briefly explains what the function does
       it is placed immediately after the function definition"""

###############DEFAULT FUNCTIONS
"""here is a short list of functions that do not require an import statement
this is not a comprehensive list"""

print max(1,2,3) #gets the max value from the inputs
print min(1,2,3)
print abs(-10)

#returns the type of the data it receives as an argument.
print type(42)
print type(4.2)
print type('spam')
print type({'Name':'John Cleese'})
print type((1,2))


#########################################SYNTAX CONVENTIONS##################################################
#for _ in range(n):
    #the _ is just a variable like any other, but by convention it means 
    #that you don't intend to use that value, just read it and ignore it.


#########################################IMPORT STATEMENTS##################################################
import math #this is called a generic import of the math module
print math.sqrt(25)  #tell Python to get the sqrt function from math

from math import sqrt#this is called a function import
#now you only have to type sqrt() to get the square root of a number
print sqrt(25)
"""
from module import * 
#this is a mixture of generic and function imports
#now you have all the tools from math but don't have to call them like you would with a generic import i.e. math.sqrt()
#do not use this if possible. If there are ever 2 functions with the same name it can be a nightmare to locate what is doing what and when.
"""

#the following is a good way to see what functions are within a module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

