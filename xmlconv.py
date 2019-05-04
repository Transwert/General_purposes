
# #Python code to illustrate parsing of XML files 
# # importing the required modules 
# import csv 
# import requests 
# import xml.etree.ElementTree as ET 
  
# def parseXML(xmlfile): 
  
#     # create element tree object 
#     tree = ET.parse(xmlfile) 
  
#     # get root element 
#     root = tree.getroot() 
  
#     # create empty list for news items 
#     mainlist = [] 
  
#     # iterate news items 
#     # for object in root.findall('//bnbbox/xmin/'): 
  
#     #     # empty news dictionary 
#     #     records = {} 

#     #     #iterate child elements of item 
#     #     for bndbox in object: 
#     #         records[bndbox.tag] = bndbox.text.encode('utf8')  

#     #     mainlist.append(records) 
#     print(root.tag)  
#     for child in root.findall("./object/*/*"):
#         print(child.tag, child.attrib)


#     #print([elem.tag for elem in root.iter()])
#     # return news items list 
#     return mainlist 
  
  
# def savetoCSV(newsitems, filename): 
  
#     # specifying the fields for csv file 
#     fields = ['name', 'pose', 'truncated', 'difficult','bndbox' ,'xmin','ymin', 'xmax','ymax'] 
  
#     # writing to csv file 
#     with open(filename, 'w') as csvfile: 
  
#         # creating a csv dict writer object 
#         writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
#         # writing headers (field names) 
#         writer.writeheader() 
  
#         # writing data rows 
#         writer.writerows(newsitems) 
  
      
# def main(): 
  
#     # parse xml file 
#     newsitems = parseXML('My photo - 09-04-2019_10-11-32.xml') 
  
#     # store news items in a csv file 
#     savetoCSV(newsitems, 'sample.csv') 
      
      
# if __name__ == "__main__": 
  
#     # calling main function 
#     main() 

import xml.etree.ElementTree as ET
import csv
from collections import Counter

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

xmlfile = "My photo - 09-04-2019_10-11-32.xml" 
items = parseXML(xmlfile)
savetoCSV(items,"output.csv")

species = [species["name"] for species in items] # for traversing list of 
print("all species provided in the file are:") 
print(species)
print("total no. of species provided are ")
print(len(species))
def unique(list1): 
    unique_list = Counter(list1).keys()
    unique_list_count = [ 1 for _  in range(len(unique_list))]
    unique_list_count = Counter(species).values()
    mergedIterator =  map(lambda n1, n2: (n1,n2), unique_list, unique_list_count)
    return list(mergedIterator)
print(unique(species))
