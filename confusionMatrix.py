import os
import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict

testDir = 'ground-truth'
validDir = 'detection-results'
Labels = 'labels.txt'

testList = []
validList = []
labelList = []
temp1 = []
temp2 = []

for n, test_file in enumerate(os.scandir(testDir)):
	testList = testList + [float(test_file.name.replace('txt', '00'))]
testList.sort()
for test_file in testList:
	temp1 = temp1 + [str(int(test_file))+".txt"]
testList = temp1

for n, valid_file in enumerate(os.scandir(validDir)):
	validList = validList + [float(valid_file.name.replace('txt', '00'))]
validList.sort()
for valid_file in validList:
	temp2 = temp2 + [str(int(valid_file))+".txt"]
validList = temp2

# print(testList)
# print(len(testList))
# print(validList)
# print(len(validList))

labelList =  [line.rstrip('\n') for line in open(Labels)]
# print(labelList)

def extractor(testDir,testList):
	sampleList = []
	for item in testList:
		with open(testDir+"/"+item,'r') as f:
			for line in f:
				for word in line.split():
					sampleList = sampleList+[word]
					break;
	return sampleList

test_result = extractor(testDir,testList)
test_result =list(set(test_result))
print("total unique items in "+ testDir +" are "+ str(len(test_result)))
#print(list(set(test_result)))

valid_result = extractor(validDir,validList)
valid_result = list(set(valid_result))
print("total unique items in "+ validDir +" are "+ str(len(valid_result)))
#print(list(set(valid_result)))

#print(labelList)
print("total unique items in "+ Labels +" are "+ str(len(labelList))+"\n")

print("since there exist between in size of number of labels and number of species in ground-truth,\ntherefore taking bigger length in consideration of confusion matrix")

def unique(list1): 
    unique_list = Counter(list1).keys()
    unique_list_count = [ 1 for _  in range(len(unique_list))]
    unique_list_count = Counter(list1).values()
    mergedIterator =  map(lambda n1, n2: (n1,n2), unique_list, unique_list_count)
    return list(mergedIterator)

# tstList = ['171.txt']
for item in testList:
	temp1 = []
	temp2 = []
	temp3 = []
	temp4 = []

	with open(testDir+"/"+item,'r') as f:
			for line in f:
				for word in line.split():
					temp1 = temp1 +[word]
					break;
	temp3 = unique(temp1)

	with open(validDir+"/"+item,'r') as f:
			for line in f:
				for word in line.split():
					temp2 = temp2 +[word]
					break;
	temp4 = unique(temp2)

	# print("test file :" + item + " - "); print(temp3)
	# print("valid file :" + item + " - ");print(temp4)

test_dict = { item : (0,0,0,0) for item in test_result}
print(test_dict)