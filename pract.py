import random
number = int(input("Введите число от 3 до 20: "))
if number > 20 or number < 3:
    number = random.randrange(3,21)
    print('Число не подходило заданным условиям, поэтому было подобрано новое число случайным образом', number)

def search_pair(num):
    result = []
    for i in range(1, num):
        for j in range(2,num):
            if i > j:
                continue
            if num % (i+j) == 0 and i != j:
                result.append(i)
                result.append(j)
    return result

print(search_pair(number))