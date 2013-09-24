#This is a single line comment
"""This
		is
			a
			   multiline 
					comment"""
#Booleans
""" True
	False
	must be capitalized
	"""
#Boolean Operators
"""
==	!=	>=	<=	<	>
and 	or		not
"""

#Strings

#convert to string =>
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