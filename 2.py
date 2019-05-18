__author__ = 'Ernie'

# Fun with functions


def doSomething():
    print()


def getList(max):
    x = list(range(max))
    for i in x:
        x[i] = i * 3
    return x

my_list = getList(10)
print(my_list)


def printPerson(name='unknown', age='unknown'):
    print("Their name is %s" % name)
    print("Their age is %s" % age)

printPerson()
printPerson("ricky")
printPerson('dave', 28)
