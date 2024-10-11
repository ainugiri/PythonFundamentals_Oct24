with open('test34.txt','r') as file1:
    lines = file1.readlines()

with open('test34.txt','w') as file1:
    for line in lines:
       if 'This is a test line 7 in the file.\n' not in line:
           file1.write(line)