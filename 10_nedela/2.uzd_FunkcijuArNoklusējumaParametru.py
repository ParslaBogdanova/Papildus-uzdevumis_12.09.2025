def greet(vards="draugs", lang="lv"):
    match lang:
        case "lv":
            return f"Sveiks, {vards}!"
        case "en":
            return f"Hello, {vards}!"
        case "de":
            return f"Hallo, {vards}!"
        case "fr":
            return f"Bonjour, {vards}!"
        case _:
            return f"Hello, {vards}!"


print(greet("Anna", "en"))
print(greet("Jānis", "lv"))
print(greet("Hans", "de"))
print(greet("Marie", "fr"))
