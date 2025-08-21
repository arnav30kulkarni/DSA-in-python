# Sets

s = set()
print (s)

# Add an item into set - O(1)

s.add(1)
s.add(2)
s.add(3)

print(s)

#Lookup in set - O(1)

if 3 in s:
    print("in set")

if 4 not in s:
    print("not in set")

# set construction - O(N)

string = "aaaaacdddsuis"

sett = set(string)
print(sett)

# Looping through set 
y=set()
y.add(1)
y.add(2)
y.add(4) 

for i in y:
    print(i)

#Hashmaps(dictionaries in python)

d = {'a':1, "b":2, "c":3}
print(d)

# Add a key val to the dictionary: O(1)

d['d'] = 4
print(d)

#check for presence in dictionary: O(1)
if 'a' in d:
    print(True)

# check value corresponding to a key in the dictionary: O(1)
print(d['a']) 

#loop over the key value pairs in dictionary: O(N)

for key, val in d.items():
    print(f'key{key}: val {val}')


# defaultdict

from collections import defaultdict

default = defaultdict(int)
default[2]
print(default)

#counter 
from collections import Counter
counter = Counter(string)

print(counter)