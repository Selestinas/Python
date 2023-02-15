nickname = 'selestina'

name = 'Kristna'

print(name, type(name))

age = 33
print(age, type(age))

date = 14.02
print(date, type(date))

b = bytes([1, 45, 75, 80])
print(b, type(b))

productlist = ['milk', 'cheese', 'cola', 'water', 'snack']
productminilist = ['ice-cream', 'melon']
print(productlist, type(productlist))
print(productminilist, type(productminilist))

result = str(name) + ' ' + nickname
print(result)

items = [nickname, name, 'Kristina', 33, ['yellow', 'orenage', 'blue'], {'age':33}, True, False, 4.5]
print(items)

s = {'ho' 'ho' 'hoy'}
print(s, type(s))
s2 = {1,2,2,2,3,4,5,6}
print(s2)
s3 = set ('kristina')
print(s3)

frozen = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
f = frozenset(frozen)
print(f)

dict = {}
dict = {'fruit': 'mango', 1: [4, 6, 8]}
print(dict)

print(str(name), age)
task12 = str(age) + name
print(task12)