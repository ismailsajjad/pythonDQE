# JSON
#dic to json
# with open('newjson.json','r') as f:
#     x= f.read()
# print(type(x))
# print(x)
# w = eval(x)
# print(type(w))
# print(w)

# make dic from string we can use Eval function

# print(eval("3+2"))
# print("3+2")
# eval("print('3+8')")
import json
a = {"1": True,"key2":None,"key4":None, 'key3':"welcome"}
# json.dump(a,open('newjson1.json','w'))
#
# c = json.load(open('newjson1.json'))
# print(c)

# newjson = json.dumps(a)
# print(type(newjson))
# print(newjson)
# <class 'str'>
# {"1": true, "key2": null, "key3": "welcome"}

# newjson1 = json.loads(newjson)
# print(type(newjson1))
# print(newjson1)
# <class 'dict'>
# {'1': True, 'key2': None, 'key3': 'welcome'}
print(json.dumps(a,indent=2))
print(json.dumps(a,indent=2,sort_keys=True))  #we can sort the JSON using sort_keys
