#reizrēķina špikeris līdz 10
number = int(input("ievadi skaitli:"))


for reizināšana in range(1,11):
    rezultāts = number * reizināšana
    print(number, "x", reizināšana, "=", rezultāts)
