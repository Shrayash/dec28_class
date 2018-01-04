lang=["Python","Java"]
creator=["Guido Van Rossum","James Goshling"]
my_dict={key:val for key, val in zip(lang,creator)}
print(my_dict)

lang=["Python","Java"]
creator=["Guido Van Rossum","James Goshling"]
my_diction={key:val for key, val in zip(lang, creator) if key !="Python"}
print(my_diction)

num=[1,2,3,4,5]
my_set={val * val for val in num}
print(my_set)
print(type(num))



str=input('Enter a name')
my_count={}

