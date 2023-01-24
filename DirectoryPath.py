import os

path = input("Enter the path to the directory: ")
filenames = os.listdir(path)

for filename in filenames:
    print(filename)
