from functools import reduce

def capitalize(item):
  return item.upper()

def higherfct(item):
  return item > 50

def accumulator(acc, item):
  return acc+item

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalize, my_pets)))
#1.1 Lamba version
print(list(map(lambda item:item.upper(), my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

zipped_list = list(zip(my_strings, my_numbers))
print(sorted(zipped_list, reverse = True))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(higherfct, scores)))
#3.1 Lamba version
print(list(filter(lambda item: item>50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
numbers = my_numbers + scores
print(reduce(accumulator, numbers))
#4.1 Labmda version
print(reduce(lambda acc,item: acc+item, numbers))
