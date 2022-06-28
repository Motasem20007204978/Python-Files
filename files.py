file = open("links.txt")
lines = file.readlines()
for line in lines:
    print(line.rstrip(" "))
print(len(lines))#sum of all readable characters
print(file.tell() - len(lines))#sum of all readable characters

print(dir(file))