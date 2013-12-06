the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through the list
for number in the_count:
    print ("This is count {}".format(number))

for fruit in fruits:
    print ("A fruit of type: {}".format(fruit))

#we can go through mixed lists  too
for i in change:
    print ("I got {}".format(i))

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print ("Adding {} to the list.".format(i))
    elements.append(i)
#or
elements = range(0,6)

#now we can print them out too
for i in elements:
    print ("Element was: {}".format(i))
