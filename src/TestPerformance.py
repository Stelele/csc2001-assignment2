import os
import random as r
import threading

fileLocation = "../input/Load_Shedding_All_Areas_Schedule_and_Map.clean.final.txt"
pathDir = "/home/gift/Documents/CSC2001F/Assignment2/input"
testPerformanceStatistics = "../output/TestPerformance.csv"

data = [line.strip() for line in open(fileLocation,'r')]

dataSpaces = len(data) // 10

#final information for each dataset
subDataSetSize = [i for i in range(0,len(data),dataSpaces)]
selectedApps = ["AVLTreeApp","BSTApp"]
selectedAppsStatistics = {app:{'comparisons':{'best':[], 'worst':[], 'average':[]},
                            {'insertions':{'best':[], 'worst':[], 'average':[]}}} for app in selectedApps}

class testRunner(threading.Thread):
    def __init__(self, threadID, fileLocation, dataSetSize):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.fileLocation = fileLocation
        self.dataSetSize = dataSetSize

    def run(self):
        dataComparisons, dataInsertions = queryDataSet(dataSetSize, selectedApps)
        best = [min(data) for ]
        threadLock.acquire()
        
        for app in selectedApps:
            selectedAppsStatistics[app]['best']



def queryDataSet(dataSetSize, apps):
    #folder locations
    tempFile = "../input/subDataSet_{}.txt".format(dataSetSize)
    tempFileLocation = pathDir+ '/' + tempFile.split("/")[-1]
    terminalOutput = "../output/terminalOutput.txt"

    subDataset = [r.choice(data) for j in range(dataSetSize)]
    
    dataComparisons = {app : [] for app in apps}
    dataInsertions = {app : [] for app in apps} 

    with open(tempFile, 'w') as f:
        f.write("\n".join(subDataset))

    for entry in subDataset:
        for app in dataComparisons.keys():
            key = entry.split(" ")[0]
            os.system("java -cp ../bin {} {} {} > {}".format(app," ".join(key.split("_")), tempFileLocation, terminalOutput))

            systemOutput = [line.strip() for line in open(terminalOutput, 'r')]

            comparisons = int(systemOutput[1].split(" ")[2])
            insertions = int(systemOutput[2].split(" ")[2])

            dataComparisons[app].append(comparisons)
            dataInsertions[app].append(insertions)

    return (dataComparisons, dataInsertions)

if __name__ == "__main__":
    main()
