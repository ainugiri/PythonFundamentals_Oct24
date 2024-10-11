import os
if os.path.exists("test34.txt"):
    os.remove("test34.txt")
else:
    print("The file does not exist")
    