import json 

file = open("sample.json","r",encoding='utf-8')

data = json.load(file)

file.close()

print(data)
print(type(data))