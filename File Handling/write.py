file = open("sample.txt","w")

l = ["Line 1", "Line 2", "Line 3"]
for item in l:
    file.write(item+"\n")

file.close()