#2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
l = [1,2,3]
a = 'abc'
l.extend('abc')
print(l)


# 3. Все чётные числа вывести в другой список
#l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
#l2=[]
    #for x in l:
            #if x%2==0: l2.append(x)
    #print(l,l2)

# 4. Все emails у которых есть слово test вывести в другой список
l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com']

for x in l:
    if x.find ('test') !=-1:
        print(x)

# 5. Найти самое маленькое число в списке
l = [3, 0, 4, 5, 8, 9, 10, 44, 22, 50, -1, 79, 54, -28, 91]
min = l[0]
for x in range(1, len(l)):
    if l[x] < min:
        min = l[x]
print(min)

# 6. Сравнить 2 строки без учёта регистра

print ('apple' == 'Aple')

# 7. Проверить является ли массив подмножеством другого массива
L1 = {1,4,6}
L2 = {9,5,1,10,4,33,2,6,0,8}

L3 = L1.issubset(L2)
print(L3)

# 8. Напишите функцию, которая принимает строку и
# возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.


l = 'abracadabra'
l2 = {}
a = set(l)

for x in a:
        if x  in 'abracadabra' and l.count(x) > 1:
                print(x, l.count(x))



print('Hello, world!')