poem = ''
fin = open("E://test.txt",'rt')
while True:
    line = fin.readline()
    if not line:
        print('can not find new line')
        break
    poem += line
    print(line)

fin.close()
print(poem,len(poem))
print(type(poem),'len :',len(poem),poem.isdigit())



print("")
print("here will be a new method :")
poem = ''
fin = open("E://test.txt",'rt')
for a in fin:
    poem +=a
    print(a)
fin.close()
print(poem,len(poem))


print("")
print("here will be a new method :")
poem = ''
fin = open("E://test.txt",'rt')
lines = fin.readlines()

for line in lines:
    poem+=line

fin.close()
print(poem,len(poem))

fin = open("E://test.txt",'rb')
data = fin.read()
print(len(data),data)
fin.close();


