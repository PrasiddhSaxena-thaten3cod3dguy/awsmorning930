prasiddh = open("test.txt","r",encoding='utf-8')

data = prasiddh.readline()
# data="BlahBlah"
# prasiddh.writelines(data)

prasiddh.close()

print(data)