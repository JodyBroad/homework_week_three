#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# add code to print a line of hyphens the same length as the Belgium string

length_of_Belgium = len(Belgium)
print(length_of_Belgium)
print(length_of_Belgium * '-')

# followed by the string with the comma separators replaced by colons ':'
print(Belgium.replace(',', ':'))

# followed by the population of Belgium (the second field) plus the population of the capital city (the fourth field)
# Hint: the answer should be 11183818.
Belgium_list = Belgium.split(",")
print(Belgium_list)
print(int(Belgium_list[1]) + int(Belgium_list[3]))
