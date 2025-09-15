name = input()
password = input()
written_password = input()
while written_password != password:
    written_password = input()
print(f"Welcome {name}!")