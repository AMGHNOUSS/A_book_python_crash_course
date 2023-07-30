name = "ada lovelace"
print(name.title())

name_0 = "Redouane AMGHNOUSS"
print(name_0.lower())
print(name_0.upper())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #is equal first_name + " " + last_name
print(full_name)
message = f"Hello, {first_name} {last_name} !"
print(message)

msg = ' python '
print(msg)
print(msg.rstrip()) # rstrtip removed a whilespace in last
print(msg.lstrip()) # rstrtip removed a whilespace in first
print(msg.strip()) # rstrtip removed a whilespace in both {first, last}

github = "https://github.com/AMGHNOUSS"
print(github)
print(github.removeprefix("https://"))