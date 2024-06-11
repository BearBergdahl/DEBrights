"""
myList = [1,2,3,4,5]
myTuple = tuple(myList)
print(myList)
print(myTuple)
print(myTuple[1])
print(myTuple.index(2))
print(len(myTuple))

for num in myTuple:
    print(num)

def myTupleReturn():
    var1 = 'ererer'
    var2 = 'hehehehe'
    var3 = 1234
    return [var1,var2,var3]

acollection = myTupleReturn()
print(acollection)
print(type(acollection))
"""
original = ['hello', 'all', 'how','are','you','this','morning' ]
copyList = original
print(id(copyList))
print(id(original))
copyList[1] = 'you'
print(original)
copyList = [3,2,5,3,66,43,9,3]

print(copyList)
print(id(copyList))

print('*************************************************')
print(original)
print(id(original))
for i in range(len(original)):
    original[i] = i+1
"""
print(original)
print(id(original))
original.append('early')
print(type(original))
print(id(original))
original = ['Hej']
print(type(original))
print(id(original))"""
print('*************************************************')
import copy
copyList = copy.copy(original)
print(copyList)
print(type(original))
print(id(original))
print(copyList)
print(type(copyList))
print(id(copyList))