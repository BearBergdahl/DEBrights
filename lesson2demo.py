# Control flows
'''
a_list_of_lines = []
while len(a_list_of_lines) == 0 :
    filename = input('Input filename: ')
    try:
        with open(filename) as afile:
            a_list_of_lines = afile.readlines()
            print(a_list_of_lines[5])
    except FileNotFoundError:
        print('Wrong filename, try again: ')
'''

for uneven in range(1,99,2):
    if uneven%3 != 0:
        print(uneven)
    else:
        print(f'This number is uneven {uneven} and divisible by 3: {uneven/2:.2f} and we have divided it in half')
  
for letter in 'banana':
    print(letter)

for fruit in ['banana', 'pineaple', 'kiwi']:
    for letter in fruit:
        print(letter)


for i in range(33,127):
    print(f'Hello {chr(i)}') 

# for loops & while loops
# if else
# or and in
# try catch
# with