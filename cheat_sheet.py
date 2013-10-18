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

######################################Booleans####################################
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


#########################################SYNTAX CONVENTIONS##################################################
#for _ in range(n):
    #the _ is just a variable like any other, but by convention it means 
    #that you don't intend to use that value, just read it and ignore it.

#########################################IMPORT STATEMENTS##################################################
import math #this is called a generic input
print math.sqrt(25)  #tell Python to get the sqrt function from math

from math import sqrt#this is called a function import
#now you only have to type sqrt() to get the square root of a number
print sqrt(25)