__author__ = 'Ernie'
# loops

x = []

for i in range(10):
    x.append(i)
    print(x)


for i in x:
    print("this index is %s" % x[i])

# dictionary
ages = {"bryan": 40, "heather": 22}

for name, age in ages.items():
    print("%s is %d years old" % (name, age))


# while
n = 0
while True:
    n += 1
    if n >= 10:
        break
    if n == 6:
        print('6 is awesome')
    print(n)
