name = input("Enter name: ").split(",")

lists = []
for n in name:
    if n in lists:
        continue
    else:
        lists.append(n)

print(lists)
