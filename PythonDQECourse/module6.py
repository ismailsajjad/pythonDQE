# #Modules and Packges

# import time
# from time import sleep as timer
# timer(0)
# print("its from from")
# time.sleep(0)
# print("after 3 sec")

# import test
# print(test.a)
#
# # sys
#
# import sys
# # print(sys.path)
# print(sys.argv)


#pip package installer for python

import os
# os.mkdir("test_new_module_6")
import json

# Create a Python dictionary (or list) with your data
data = {
    "name": "Ismail",
    "age": 30,
    "city": "New York"
}

# Specify the file path where you want to write the JSON data
file_path = "test_new_module_6/Latest_News"

# Open the file in write mode and use 'json.dump()' to write the data
with open(file_path, "w") as json_file:
    json.dump(data, json_file)

print(f"Data has been written to {file_path}")
#open()
# with open('test_new_module_6/Latest_News', 'w') as a:
#     print(a.read())
