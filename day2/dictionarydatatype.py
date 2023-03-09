#Dictionary :- To look the meaning 

dict1={
        "Name": "Prasiddh",
        "Age": 22
}
print(dict1)

print(dict1["Name"])

agiladict={
    "Name":"Agila",
    "Age" :23,
    "Gender":"Female",
    "Siblings":{
        "Name":"Raj",
        "Age":27,
        "Hobbies":["Music"]
    },
    "Hobbies":["Drawing","Dancing"]
}

print(agiladict["Gender"])
print(agiladict["Hobbies"][1])
print(agiladict["Siblings"]["Age"])
print(agiladict["Siblings"]["Hobbies"][0])

#Functions
#1. keys() --> Return list of key in the dictionary

print(agiladict.keys())

#Adding new keys to existing dictionary

agiladict["Course"]="AWS"

print(agiladict)

