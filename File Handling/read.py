# r+ for both reading and writing
file = open("sample.txt",'r')



content = file.readlines()
print(content)

content = [i.rstrip('\n') for i in content]
print(content)

file.close()