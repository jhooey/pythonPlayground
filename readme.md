#Keywords#

##and##
the conditions on both sides of this keyword need to be met for the boolean
expression to return true

##del##
The del keyword deletes objects.

Ex:
```
a = [1,2,3,4]
print a
>>> [1, 2, 3, 4]
del a
print a
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> NameError: name 'a' is not defined
```

##from##
The from keyword is used for importing a specific variable, class or a function from a module.

Ex:
from sys import version

##not##
The not keyword negates a boolean value

Ex:
not True -> False

##while##
The statements inside the while loop are executed, until the expression evaluates to False.

##as##
The as keyword is used if we want to give a module a different alias.

Ex:
import random as rnd

##if##
The if keyword is used to determine, which statements are going to be executed.

##elif##
elif keyword. Stands for else if.

##else##
If none of the if tests are True, the else statement is executed

##global##
If we want to access variables defined outside functions, we use the global keyword.

Ex:
x = 15

def function():
   global x
   x = 45

function()
print x

##or##
only one of the conditions on both sides of this keyword need to be met for the boolean
expression to return true

##with##
Python’s with statement was first introduced five years ago, in Python 2.5. It’s handy when you have two related operations which you’d like to execute as a pair, with a block of code in between. The classic example is opening a file, manipulating the file, then closing it:

Ex:
with open('output.txt', 'w') as f:
    f.write('Hi there!')
	
The above with statement will automatically close the file after the nested block of code. (Continue reading to see exactly how the close occurs.) The advantage of using a with statement is that it is guaranteed to close the file no matter how the nested block exits. If an exception occurs before the end of the block, it will close the file before the exception is caught by an outer exception handler. If the nested block were to contain a return statement, or a continue or break statement, the with statement would automatically close the file in those cases, too.

##assert##
The assert keyword is used for debugging purposes. We can use it for testing conditions, that are obvious to us.

Ex:
For example, we have a program that calculates salaries. We know that the salary cannot be less than zero. So we might put such an assertion to the code. If the assertion fails, the interpreter will complain.

salary = 3500
salary -= 3560 # a mistake was done

assert salary > 0

Traceback (most recent call last):
  File "./salary.py", line 9, in <module>
    assert salary > 0
AssertionError

##pass##
The pass keyword does nothing. It is a very handy keyword in some situations.

Ex:
 def function():
     pass
We have a function. This function is not implemented yet. It will be later. The body of the function must not be empty. So we can use a pass keyword here, instead of printing something like "function not implemented yet" or similar.

##yield##
###Iterables###

When you create a list, you can read its items one by one, and it's called iteration:
```
>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3
```

Mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable:

```
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
```
Everything you can use "for... in..." on is an iterable: lists, strings, files... These iterables are handy because you can read them as much as you wish, but you store all the values in memory and it's not always what you want when you have a lot of values.

###Generators###

Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly:

```
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```

It is just the same except you used () instead of []. BUT, you can not perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

###Yield###
Yield is a keyword that is used like return, except the function will return a generator.

```
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to read once.

To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

Then, your code will be run each time the for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy a "if/else" anymore.


##break##
The break keyword is used to interrupt the cycle (ie. jump out of a loop)

##try##
A block of code that runs unless an exception is thrown.


##except##
If an error is encountered, a try block code execution is stopped and transferred
down to the except block. 

##finally##
In addition to using an except block after the try block, you can also use the
finally block. 

The code in the finally block will be executed regardless of whether an exception
occurs.

##import##
The import keyword is used to import other modules into a Python script.

##class##
The class keyword is the most important keyword in object oriented programming. It is used to create new user defined objects.

##exec##
The exec statement is used to execute Python statements which are stored in a string or file. For example, we can generate a string containing Python code at runtime and then execute these statements using the exec statement. 

Ex:
```
>>> exec 'print "Hello World"'
Hello World
```

###eval###
The eval statement is used to evaluate valid Python expressions which are stored in a string
Ex:
```
>>> eval('2*3')
6
```

##in##
The in key word can be used as a boolean expression 

Ex:
```
>>> print 4 in (2,3,5,6)
False
```

Or it can be used to iterate a loop

```
Ex:
>>> myList = [1,2,3]
>>> for i in myList:
...     print i,
...
1 2 3
```

##raise##
The raise keyword has 2 purposes.

1. It's used for raising your own errors.
```
if something:
    raise error('My error!')
```
2. It's used to re-raise the current exception in an exception handler, so that it can be handled further up the call stack.

```
try:
  generate_exception()
except SomeException, e:
  if not can_handle(e):
    raise
  handle_exception(e)
```

##continue##
the continue keyword is used to interrupt the current cycle, without jumping out of the whole loop. New cycle will begin

##is##
is tests for identity, not equality. That means Python simply compares the memory address a object resides in. is basically answers the question "Do I have two names for the same object?"

##return##
The return key is closely connected with a function definition. The keyword exits the function and returns a value.

##def##
The def keyword is used to create a new user defined function. Functions are objects in which we organize our code.

##for##
The for keyword is used to iterate over items of a collection in order that they appear in the container.

##lambda##
What lambda does is that it defines an anonymous function object on the spot. 


#Operators#

## Arithmetic Operators ##
* +		- Addition - Adds values on either side of the operator
* - 	- Subtraction - Subtracts right hand operand from left hand operand
* \*	- Multiplication - Multiplies values on either side of the operator
* \*\*	- Exponent - Performs exponential (power) calculation on operators
* /		- Division - Divides left hand operand by right hand operand
* //	- Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
* %		- Division - Divides left hand operand by right hand operand

## Comparison Operators ##
* <		- Checks if the value of left operand is less than the value of right operand, if yes then condition becomes true.
* >		- Checks if the value of left operand is greater than the value of right operand, if yes then condition becomes true.
* <=	- Checks if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true.
* >=	- Checks if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true.
* ==	- Checks if the value of two operands are equal or not, if yes then condition becomes true.
* !=	- Checks if the value of two operands are equal or not, if values are not equal then condition becomes true.
* <>	- Checks if the value of two operands are equal or not, if values are not equal then condition becomes true.  (REMOVED IN PYTHON 3)

## Assignment Operators ##
* =		- Simple assignment operator, Assigns values from right side operands to left side operand
* +=	- Add AND assignment operator, It adds right operand to the left operand and assign the result to left operand
* -=	- Subtract AND assignment operator, It subtracts right operand from the left operand and assign the result to left operand
* \*=	- Multiply AND assignment operator, It multiplies right operand with the left operand and assign the result to left operand
* /=	- Divide AND assignment operator, It divides left operand with the right operand and assign the result to left operand
* //=	- Floor Dividion and assigns a value, Performs floor division on operators and assign value to the left operand
* %=	- Modulus AND assignment operator, It takes modulus using two operands and assign the result to left operand
* \*\*=	- Exponent AND assignment operator, Performs exponential (power) calculation on operators and assign value to the left operand

## Other Symbols ##
* @		- signifies a python decorator - good explination here: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
* ;		- Python does not require semi-colons to terminate statements. Semi colons can be used to delimit statements if you wish to put multiple statements on the same line.


#Data Types#
##Tuples##
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example:

##Lists##
Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ( [ ] and [ : ] ) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus ( + ) sign is the list concatenation operator, and the asterisk ( * ) is the repetition operator. For example:

##Python Dictionary##
Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ( { } ) and values can be assigned and accessed using square braces ( [] ). For example:

