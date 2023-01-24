import os
from datetime import datetime

path = input("Please enter the pathname")
your_sentence = input("what to type in?")
x = datetime.now()
file_name = x.strftime('%d-%m-%y.txt')
file_path = os.path.join(path, file_name)
if os.path.exists(file_path):
    print(f"file {file_name}already exists in {file_path}")
else:
    try:
        with open(file_path, 'w') as fp:
            fp.write(your_sentence)
    except:
            print(f"Error while trying to create {file_name}")
