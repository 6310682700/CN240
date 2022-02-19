import glob
import os
  
  
print('Named explicitly:')
for name in glob.glob('/Desktop'):
    print(name)
  
# Using '*' pattern 
print('\nNamed with wildcard *:')
for name in glob.glob('/Users/Allumile/Desktop/facial_expressions/images/*'):
    print(name)
  
# Using '?' pattern
print('\nNamed with wildcard ?:')
for name in glob.glob('/home/geeks/Desktop/gfg/data?.txt'):
    print(name)
  
# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for name in glob.glob('/home/geeks/Desktop/gfg/*[0-9].*'):
    print(name)

arr = os.listdir('/Users/Allumile/Desktop/facial_expressions/images')
print(arr)