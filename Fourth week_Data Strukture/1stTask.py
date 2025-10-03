while True:
    skaitlis = list(map(int, input("Ievadiet veselus skaitļus: ").split()))
    if skaitlis == 0:
        break
    lists = sorted(skaitlis)
    print(lists)
