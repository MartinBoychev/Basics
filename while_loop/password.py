name = input()
password = input()
guess_pass = input()

while guess_pass != password:
    guess_pass = input()
print(f"Welcome {name}!")