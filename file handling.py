fp=open("d:\\new_text.txt","w")
print(fp)

fp.write("hello world, agains")
fp.close()

f=open("d:\\new_text.txt","r")
print(f.read())
f.close()

f=open("d:\\new_text.txt","a")
print(f)
f.write(" appending")
f.close()

f=open("d:\\new_text.txt","r")
print(f.read())
f.close()

fp=open("d:\\new.txt","w")
fp.write("Hello World")
print(fp.tell())
fp.close()

with open('some_file.txt','w') as fp:
    fp.write('hello world')
l=["Hello","There"]
with open("list.txt","w") as fp:
    for each in l:
        fp.write(each)
