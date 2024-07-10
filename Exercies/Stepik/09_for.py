avengers = ["Tony", "Piter", "James", "John", "Malcolm", "Gina"]

for f in avengers:
    if f == "Gina":
        print(f"{f} is bitch!")
    else:
        var = f + " is asshole"
        print(var)
print()
for f in avengers[0:3]:
    if f == "Gina":
        print(f"{f} is bitch!")
    else:
        var = f + " is asshole"
        print(var)
print()
for f in avengers[2:]:
    if f == "Gina":
        print(f"{f} is bitch!")
    else:
        var = f + " is asshole"
        print(var)
print()
for f in avengers:
    print(len(f)) #Вывод в консоль длины каждого элемента.