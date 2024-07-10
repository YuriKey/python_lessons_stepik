# fw = open('files/file.txt', 'a')
# fw.write('hello neo\n')
# fw.close()

# var = input("what is your name? ")
# fw = open('files/file.txt', 'a')
# fw.write(var)
# fw.close()
#
# var = input("what is your name? ")
# fw = open('files/file1.txt', 'w')
# fw.write(var)
# fw.close()


fw = open('../../files/file.txt', 'r+')
var = fw.read()
fw.write('hello neo\n')
fw.write('but i`m chuck\n')
fw.close()
print(var)
