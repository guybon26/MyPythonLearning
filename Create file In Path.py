import os

path = input("Enter the path to the directory: ")
file_name = input("enter the file name you would like")
your_sentence = input("what would you like to write in it?")

if os.path.exists(os.path.join(path, file_name)):
    print("file already exists")
else:
    with open(os.path.join(path, file_name), 'w') as fp:
        fp.write(your_sentence)

pass