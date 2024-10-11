with open('test34.txt','a') as file1:
    file1.write("This is a test line 1 in the file.\n")
    file1.write('This is a test line 2 in the file.\n')
    file1.write('This is a test line 3 in the file.\n')
    file1.write('This is a test line 4 in the file.\n')
    
with open('test32.txt','r') as file1:
    content = file1.read()
    print(content)
    