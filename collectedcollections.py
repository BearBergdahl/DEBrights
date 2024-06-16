
foodlist = []
with open("food.txt") as myfile:
    foodlist = myfile.readlines()

foodstuff = set()

for line in foodlist:
    a, _ = line.split(':')
    foodstuff.add(a)

print(foodstuff)

raw_foodcount = len(foodlist)
foodcount = len(foodstuff)
print('total: ', raw_foodcount," and unique: " ,foodcount)

indexed_foodstuff = zip(foodstuff, range(foodcount))
food_dict = dict()
for each_tuple in indexed_foodstuff: 
    print(each_tuple)
    food_dict.update([each_tuple])

new_food_list = []
for line in foodlist:
    ingredient, measure = line.split(':')
    ingredient = food_dict[ingredient]
    new_food_list.append(f'{ingredient} : {measure}')

print(new_food_list)
