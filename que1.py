value=lambda x,y: x if x>y else y
value(2,3)
print(value(2,3))

value1=lambda x,y: x/y if y!=0 else "zer0 division error"
value1(2,3)
print(value1(2,3))

x=[1,2,3]
x_new=[]
def sqr(i):
    return i * i
for each in x:
    x_new.append(sqr(each))
print(x_new)

x_new=map(sqr,x)
print(list(x_new))

print(list(map(lambda n:n**2,x)))

c=[1,2,3,4,5,6]
print(list(filter(lambda x:x % 2==0, c)))

l=["hello","world","hola"]
print(list(filter(lambda l: l.startswith("h"),l)))

