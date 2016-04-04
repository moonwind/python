import os
print('Hello World')
byte = bytes(range(0,256))
print(len(byte))

fout = open("D://testwrite.bin",'wb')
num = fout.write(byte)
if num!=len(byte):
    print('write error')
print('write ok');
fout.close();


offsize =0 
chunk = 30
byte = bytes(range(0,256))
size = len(byte)
print(len(byte))

fout = open("D://testwrite.bin",'wb')

while True:
    if(offsize >=size):
        break;
    print(byte[offsize:offsize+chunk])
    readNum =fout.write(byte[offsize:offsize+chunk])
    offsize+=readNum 
    print("offsize",offsize,"readNum :",readNum)

print('write ok');
fout.close();