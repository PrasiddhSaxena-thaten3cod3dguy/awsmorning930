import json

dict1={
    "name": "Prasiddh",
    "Age" : 22
}

file = open("sample.json","w",encoding='utf-8')

file.write(json.dumps(dict1,indent=4))
# file.write(dict1)

file.close()