#following file on execution, creates a csv file for the coresponding XML file provided,
#with giving the distinct number of cells and their respective numbers in the XML file 
import os.path
import glob
from os import path
from pathlib import Path
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

    print("All species provided in the file are:") 
    print(species)
    print("Total no. of species provided are ")
    print(len(species))
    print(unique(species))
    print("\n")

