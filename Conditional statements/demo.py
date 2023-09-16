myTextBlock = """
    Hey, My name is Kristaps
    I am teaching Python on September {}, {}!

    Es mācu Piton valodu kiberdrošības ekspertiem.
""".format(9, 0)

a = "A"
b = "B"

twentyA = a * 20

print(a + b)
print(twentyA)
print(myTextBlock)

myName = "Kristaps"

print(myName[0:len(myName):2])

print(int("9"))
print(str(9))

aSentence = "My name is Kristaps"
parts = aSentence.split(" ")
print(parts)

findResult = aSentence.find(" ")
print("The character was found at position {}".format(findResult))

# res = aSentence.split(" ")[0].find("is")

ip = "127.0.0.1"

bSentence = "My IP is: %s" % ip

print(bSentence)

aTwo = 2
res = 2**4
print(res)

a = True
b = False

if a or b:
    print("both true either one or the other is true")
else:
    print('either a or b is false')


a = 1
b = 2

a+=1
a = a+1

print(a)

myList = [1, [3, 4, "Security"], [3, 4], 2, 3]
print(myList)
print(len(myList[1][2]))

del myList[1]
print(myList)


course = ("Information Security", 82838, 10, 2)
print(course)

subject, code, month, day = course

print("""
    Unpacking done for fields:
        subject: {}
        code: {}
        month: {}
        day: {}
""".format(subject, code, month, day))

listOfNumbers = [1, 2, 3, 3, 4, 5, 5]
print(listOfNumbers)
print(list(set(listOfNumbers)))


listOfNumbersNext = [4, 5, 6, 7, 9, 0]

print(set(listOfNumbers) - set(listOfNumbersNext))

myDictionary = {
    "name": "Kristaps",
    "age": 31,
    "role": {
        "code": 1234,
        "name": "Teacher"
    }
}

print(myDictionary)
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary["name"])
print(myDictionary.items())

for entry in myDictionary.items():
    print("key: {}".format(entry[0]))
    print("val: {}".format(entry[1]))


for entry in myDictionary.items():
        print("key: {}".format(entry[0]))
        print("val: {}".format(entry[1]))

if True:
    print(1)
elif False:
    print(2)
elif False:
    print(2)

# print(dir(myDictionary))


# for i in range(1,10):
#     print(i)

i=0
while i < 10:
    print(i)
    i+=1
    if i == 5:
        pass

else:
    print("ended with {}".format(i))


for x in [1, ["a", "b", "c"], 3, 4]:
    print(x)
    if isinstance(x, list):
        for y in x:
            print(y)

print("-------------------------")
for x in enumerate([1, ["a", "b", "c"], 3, 4]):
    print(x)
