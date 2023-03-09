#Strings :- Collection of Characters

mystring="Hi My name is Prasiddh"

print(mystring)
print(type(mystring))

#Operations

#String Concatenation:- To add 2 or more strings together
string1="Hello"
string2="World"
result= string1 + " " +string2
# print(result)

#String Duplication:- String needs to be repeated multiple times.

string1="My World is beautiful "
print(string1*20)

#Question:-
result= "2" + "2"
print(result)

string3="Hello world"
string4=string3 * 10

print(string4)

#Multiline String

string5="""
Hi My name is Prasiddh Saxena
I am an ethical hacker
 """
print(string5)

#Sigle Quotes , Double Quotes , Triple Quotes? --> Expirement

string6='Hi, This computer belongs to prasiddh"s dad'
print(string6)

#Functions
#len() ---> Length of the string
string7="Hello "
print(len(string7))

#strip() --> It remove white spaces from the string from end corners
string8="          Hello                     "
print(string8.strip())

#split()

#upper() --> Convert all the char in the string in upper case i.e. capital letters

string9="hello"
print(string9.upper())

#lower() -->Convert all the char in the string in lower case i.e. normal letters
string10="Hello"
print(string10.lower())
