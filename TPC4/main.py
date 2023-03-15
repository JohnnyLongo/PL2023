import re
import json

input_file = open("C:/Users/longu/OneDrive/Documents/GitHub/PL2023/TPC4/input.csv", "r")
output_file = open("C:/Users/longu/OneDrive/Documents/GitHub/PL2023/TPC4/output.json", "w")
line_list = input_file.readlines()
input_file.close()
atri_names = re.split(",", line_list[0], 0)         #get attribute names
i = 1
dict = {}
while i < len(line_list):
    atri_values = re.split(",", line_list[i], 0)    #get values for object instance no. i
    name = "obj"+str(i)                             
    obj_dict = {}
    j = 0
    while j < len(atri_values):
        if(re.search("\n", atri_names[j])):
            atri_names[j] = (re.split("\n", atri_names[j], 1))[0]       #cut \n at the end of strings for pretty
        if(j < len(atri_values) and re.search("\n", atri_values[j])):
            atri_values[j] = (re.split("\n", atri_values[j], 1))[0]

        if(re.match("[a-zA-Z]+\{[0-9]+\}", atri_names[j])):
            temp = (re.split("\{", atri_names[j], 0)[1])
            listlen = int (re.split("}", temp, 0)[0])
            k = 0
            list_attribute = []
            list_name = (re.split("\{", atri_names[j], 0)[0])
            while k < listlen:
                k+=1

                list_attribute.append(atri_values[j])

                j+=1
            print("banana")
            obj_dict[list_name] = list_attribute
        else:
            obj_dict[atri_names[j]] = atri_values[j]
            j+=1
    dict[name] = obj_dict                                               #put all instances in a dictionary
    i+=1                                                                #(makes dump easier)
json.dump(dict, output_file, indent = 6)
output_file.close()
