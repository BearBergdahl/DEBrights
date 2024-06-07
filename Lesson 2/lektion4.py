# demo 1

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

#demo 2
my_list = [2,4,8,0,1]
for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(my_list[i])

for i in [2,4,8,0,1]:
    print(i)

if 4 in my_list:
    print('It´s there!')
if 6 not in my_list:
    print('It´s not there!')

#demo3 listor


    
    


