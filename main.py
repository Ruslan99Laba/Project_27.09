# 1 Задание

my_list = [1, 5, 110, 432, 3, 7, 253, 974, 9, 512, 8, 2]
for i in my_list:
    if i > 100:
        print(i)

print('\n')

# 2 Задание


my_list = [2, 438, 53, 123, 1, 55, 654, 7, 584, 974, 4]
my_results = []

for i in my_list:
    if i > 100:
        my_results.append(i)
for i in my_results:
    print()

print(my_results)

print('\n')

# 3 Задание

my_list = [1, 2, 3, 4, 5, 6]

if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)

print(my_list)

print(sum(my_list[-2:]))

print('\n')

