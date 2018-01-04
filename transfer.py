with open("d:\\test.txt","w") as fp:
    fp.write("hello World")


with open("d:\\test.txt","r") as fp:
    list=[]
    list=fp.read()
    print("",list)

with open("d:\\new_text.txt","w") as f:
    f.write(list)




