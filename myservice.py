#import libraries
import sys, getopt, re, json, io

#define main 
def main(argv): #main function
	g = Graph() #created an instance from the class
	g.createLists(sys.argv[1]) #create the lists from the file
	g.makeMasterDictionary() #create the dictionary of lists
	g.createJsonFile() #create the json file
		
	
class Graph:
	#create objects
	graph={}
	srcList=[]
	destList=[]
	weightList=[]
	nodeList = []

	
	
	def __init__(self): 
	#create the constructor
		self.graph={}
		self.srcList=[]
		self.destList=[]
		self.weightList=[]
		self.nodeList = []

		self.anotherDict={}
		self.anotherList=[]

	def createLists(self,path): 
		#read the file into list and create the lists
		file=open(path)
		for line in file.readlines():
			node1, node2, weight=line.split(" ")
			node1=int(node1)
			node2=int(node2)
			weight=int(weight)
			self.srcList.append(node1)
			self.destList.append(node2)
			self.weightList.append(weight)
			if node1 not in self.nodeList:
				self.nodeList.append(node1)
			if node2 not in self.nodeList:
				self.nodeList.append(node2)
		file.close()

	def makeMasterDictionary(self):
		#create the list of dictionary first:
		size=len(self.nodeList)
		tempDict={}
		tempList=[]
		otherDict={}
		otherList=[]

		for i in range(size):
			tempDict["" "label" ]=self.nodeList[i]
			tempDict["" "group"  ]= 0
			tempList.append(tempDict.copy())

			#print self.tempDict, "\n"
			#each element in the src list and weight list is an item in the tempdict.
			#add the tempdict into the temp list
		#print tempList
		self.graph["nodes"]=tempList


		#for each...find the source/dest list = to the node list...get the index number...save that.
		src_size = len(self.srcList)
		dest_size = len(self.destList)
		for i in range(src_size):
			if self.srcList[i] in self.nodeList:
				emp=self.srcList[i]
				otherDict["" "source"]= self.nodeList.index(emp)
			if self.destList[i] in self.nodeList:
				temp=self.destList[i]
				otherDict["" "target"]=  self.nodeList.index(temp)
			otherDict["" "value"]=self.weightList[i]
			otherList.append(otherDict.copy())
		self.graph["links"]=otherList


	def createJsonFile(self):
		with open ("hello.json", "w") as outfile:
  			outfile.write(unicode(json.dumps(self.graph, sort_keys = False, skipkeys=True, ensure_ascii=True, check_circular=True, 
  				allow_nan=True, cls=None, indent=2, separators=None, encoding='utf-8', default=None)))
  		outfile.close()



if __name__ == "__main__": #this is the main function
	main(sys.argv[1:])