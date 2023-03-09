#List
list1=[1,2,3,"Legends Never Die",4]

print(list1[3])

list2=[1,2,3,4,5,6,7,8,9]

print(list2[5])

list3=[]
list4=[1]

print((list3))
print(list4)

#Errors Possible 
# print(list1[100])

#Functions

#1. append()  --> Add Values to the list

list5=[1,2,3,4]
print(list5)
list5.append("Raghav doubt clear?")
print(list5)
print(list5)

#2. insert()

list5.insert(3, "Shashank")
print(list5)

#List of Available Functions
# print(help(list))

#3. pop() --> Delete the element

list6=[4,5,6,7,8]
print(list6)
list6.pop()
print(list6)

#4. remove() --> Delete the element from particular element in the list
list6.remove(6)
print(list6)

#Nested List:- List Inside List

list7=[1,2,3,4,5,["Joker","Thanos","Hulk"]]
print(list7[5][1])

list7[0]="Prasiddh"

# list7.append([11,12,13])
print(list7)





