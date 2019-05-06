# following file on execution, creates a csv file for the coresponding XML file provided,
# with giving the distinct number of cells and their respective numbers in the XML file 
# and save the summary in .txt file 
import os.path
import glob
from os import path
from pathlib import Path
import xml.etree.ElementTree as ET
import csv
from collections import Counter
from collections import defaultdict

total_list = [] 
temp_list = []
def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    mainlist = []

    for object in root.findall('.//object'):
        records = {}
        for node in object:

            if (len(node.findall("*"))>0):

                for subnode in node.findall('*'): # for finding children in the node accessed and recording their data
                    records[subnode.tag] = subnode.text.encode('utf8')
            else: # for finding data directly from node
                records[node.tag] = node.text.encode('utf8')

        mainlist.append(records)
    #print(mainlist)
    return mainlist

def savetoCSV(newsitems, filename):
    fields = ['name', 'pose', 'truncated', 'difficult', 'xmin','ymin', 'xmax','ymax']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(newsitems)

def unique(list1): 
    unique_list = Counter(list1).keys()
    unique_list_count = [ 1 for _  in range(len(unique_list))]
    unique_list_count = Counter(species).values()
    mergedIterator =  map(lambda n1, n2: (n1,n2), unique_list, unique_list_count)
    return list(mergedIterator)


address = glob.glob('*.xml')
#print(address)
for single_add in address:
    xmlfile = single_add  
    items = parseXML(xmlfile)
    savetoCSV(items,"output.csv")
    species = [species["name"] for species in items] # for traversing list of all species in XML files
    temp_list = temp_list + species
    total_list = total_list + unique(species)
    print(single_add)
    print("All species provided in the file are:") 
    print(species)
    print("Total no. of species provided are ")
    print(len(species))
    print(unique(species))
    print("\n")

temp_list = Counter(temp_list).keys()
result = defaultdict(int) 
for key, value in total_list: 
    if key in temp_list:
        result[key] += value
print(result)

with open('summary.txt', 'a') as out_file:
    out_file.write("Total no. of species provided are\n{}\n{}\n and each species are in total:\n{}".format(
        len(temp_list),temp_list,result))

# this below dumped part of code which was alternative of above which was not working.

#print(temp_list)
# print("\n")
# print(total_list)

# def ispresent(key,list):
#     for qwerty in list:
#         if qwerty == key:
#             return 1
#         else:
#             return 0

# def indexreturn(key,list):
#     counter = 0
#     for qwerty in list:
#         if qwerty != key:
#             counter = counter + 1
#         else:
#             return counter

# def mult_indexreturn(key,list):
#     for i in range(len(list)):
#         if key == list[i][0]:
#                 return i

# final = [(1,0),(2,3),(7,8),(6,0)]
# #print(mult_indexreturn(,final))
# # print(ispresent((4,2),final))

# print(temp_list[0])
# final = map(lambda n1, n2: (n1,n2 ), temp_list,[ 0 for _  in range(len(temp_list))])
# for object2 in total_list:
#     for object1 in temp_list:
#         if object2 == object1:
#             final[  indexreturn(object2,final) ][1] = final[  indexreturn(object2, final)  ][1] + object2[mult_indexreturn(object2,total_list)][1]#total_list[ mult_indexreturn(object2,total_list) ][1]
# print(final)




