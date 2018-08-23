#ques 1
dict={"apple":"green","banana":"yellow","cherry": "red"}
list=[]
for i in dict.keys():
    list.append(i)
print(list)

#ques 2

people = {'Tajinder': {'maths':'99', 'english': '99', 'science': '99'},
          'simran.T': {'maths':'33', 'english': '33', 'science': '33'}}
print(people['Tajinder']['maths'],people['Tajinder']['english'],people['Tajinder']['science'])
print(people['simran.T']['maths'],people['simran.T']['english'],people['simran.T']['science'])


