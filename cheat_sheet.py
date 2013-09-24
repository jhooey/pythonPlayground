#This is a single line comment
"""This
		is
			a
			   multiline 
					comment"""
					
#####################################Date and Time################################
from datetime import datetime

now = datetime.now()
print(now)
month 	= now.month
day 	= now.day
year	= now.year
hour	= now.hour
minute	= now.minute
second	= now.second
print (str(month) + "/" + str(day) + "/" + str(year) + " " + str(hour) + ":" + str(minute) +":"+ str(second))

######################################Booleans####################################
""" True
	False
	must be capitalized
	"""
#Boolean Operators
"""
==	!=	>=	<=	<	>
and 	or		not
"""

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
print(fifth_letter)
fifth_letter = "MONTY"[-1]#you can also start from the end of the string
print(fifth_letter)
substring = "MONTY"[1:-1]#you can also select a substring
print(substring)
substring = "MONTY"[1:] #select a substring from index 1 to the end of the string
print(substring)

#Get the length of a string
print (len(substring))
#Convert string to all lowercase
print (substring.lower())
#Convert string to all uppercase
print (substring.upper())

# The % string formatter replaced the %s (the "s" is for "string") in our string with the variables in parentheses.
string_1 = "Camelot"
string_2 = "place"
string_3 = "Let's not go to %s. 'Tis a silly %s."
string_4 = "Holland"
string_5 = "place"
print (string_3 % (string_1, string_2))
print (string_3 % (string_4, string_5))


