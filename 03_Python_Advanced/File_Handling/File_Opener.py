import os


# if os.path.exists("text.txt"):
#     print("File Found")
#
# else:
#     print("File not found")

try:
    file = open("text.txt")

    print("File Found")
except FileNotFoundError:
    print("File not found")





