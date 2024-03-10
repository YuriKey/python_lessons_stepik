file_name = 'files/file2.txt'
data = "hello neo\n"

# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'a') as files:
    files.write(data)