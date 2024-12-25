x = 5
print(type(x))

num = 3.14159
print(round(num, 2))

square = [x ** 2 for x in range(10)]
print(square)

numbers = (1, 2, 3)
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


my_list = [1, 2, 3, 4]
print(len(my_list))


x = 1
while x < 10:
    print(x)
    x = x + 1


name = ('a,' 'b,' 'c,' 'd')
for x in name:
    print(x)