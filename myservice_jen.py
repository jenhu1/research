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

	
	
	def __init__(self): 
	#create the constructor
		self.graph={}
		self.srcList=[]
		self.destList=[]
		self.weightList=[]

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
		file.close()

	def makeMasterDictionary(self):
		#create the list of dictionary first:
		size=len(self.srcList)
		tempDict={}
		tempList=[]
		otherDict={}
		otherList=[]

		for i in range(size):
			tempDict[" ""label" ]=self.srcList[i]
			tempDict[" ""group"  ]=self.weightList[i]
			tempList.append(tempDict.copy())
			#print self.tempDict, "\n"
			#each element in the src list and weight list is an item in the tempdict.
			#add the tempdict into the temp list
		#print tempList
		self.graph["nodes"]=tempList

		
		for i in range(size):
			otherDict[" ""source"]=self.srcList[i]
			otherDict[" ""target"]=self.destList[i]
			otherDict[" ""value"]=self.weightList[i]
			otherList.append(otherDict.copy())
			#print self.tempDict, "\n"
			#each element in the src list and weight list is an item in the tempdict.
			#add the tempdict into the temp list
		#print tempList
		self.graph["links"]=otherList

	

	def createJsonFile(self):
		with open ("hello.json", "w") as outfile:
  			outfile.write(unicode(json.dumps(self.graph, skipkeys=False, ensure_ascii=True, check_circular=True, 
  				allow_nan=True, cls=None, indent=0, separators=None, encoding='utf-8', default=None)))
  		outfile.close()



if __name__ == "__main__": #this is the main function
	main(sys.argv[1:])