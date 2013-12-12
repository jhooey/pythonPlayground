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

##continue##
the continue keyword is used to interrupt the current cycle, without jumping out of the whole loop. New cycle will begin


##is##

##return##

##def##

##for##

##lambda##




#String Escape Sequences#

* \\ - 
* \' - '
* \" - "
* \a
* \b
* \f
* \n
* \r
* \t
* \v

#Operators#

* +
* -
* *
* **
* /
* //
*   %
    <
    >
    <=
    >=
    ==
    !=
    <>
    ( )
    [ ]
    { }
    @
    ,
    :
    .
    =
    ;
    +=
    -=
    *=
    /=
    //=
    %=
    **=

