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
                                'insertions':{'best':[], 'worst':[], 'average':[]}} for app in selectedApps}
dataSetSizeOrder = []

class testRunner(threading.Thread):
    def __init__(self, threadID, dataSetSize):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.fileLocation = fileLocation
        self.dataSetSize = dataSetSize

    def run(self):
        dataComparisons, dataInsertions = queryDataSet(self.dataSetSize, selectedApps)
        threadLock.acquire()
        
        dataSetSizeOrder.append(self.dataSetSize)

        for app in selectedApps:
            selectedAppsStatistics[app]['comparisons']['best'].append(min(dataComparisons[app]))
            selectedAppsStatistics[app]['comparisons']['worst'].append(max(dataComparisons[app]))
            selectedAppsStatistics[app]['comparisons']['average'].append(sum(dataComparisons[app])//len(dataComparisons[app]))

            selectedAppsStatistics[app]['insertions']['best'].append(min(dataInsertions[app]))
            selectedAppsStatistics[app]['insertions']['worst'].append(max(dataInsertions[app]))
            selectedAppsStatistics[app]['insertions']['average'].append(sum(dataInsertions[app])//len(dataInsertions[app]))

        threadLock.release()

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
        for app in apps:
            key = entry.split(" ")[0]
            threadLock.acquire()
            os.system("java -cp ../bin {} {} {} > {}".format(app," ".join(key.split("_")), tempFileLocation, terminalOutput))
            threadLock.release()

            systemOutput = [line.strip() for line in open(terminalOutput, 'r')]

            comparisons = int(systemOutput[1].split(" ")[2])
            insertions = int(systemOutput[2].split(" ")[2])

            dataComparisons[app].append(comparisons)
            dataInsertions[app].append(insertions)
        
    return (dataComparisons, dataInsertions)

if __name__ == "__main__":
    threads = []
    threadLock = threading.Lock()
    
    print("Welcome to Test Performance\nStarting to test runner apps")
    for index, size in enumerate(range(dataSpaces, len(data), dataSpaces)):
        threads.append(testRunner(index,size))
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
    print("Testing done. Outputing results to {}".format(testPerformanceStatistics))
    with open(testPerformanceStatistics, 'w') as f:
        f.write(",{}\n".format(",".join(map(str,dataSetSizeOrder))))

        for app,operations in selectedAppsStatistics.items():
            for operation, case in operations.items():
                rowName = app + ' ' + operation
                f.write("{},{}\n".format(rowName + ' best', ",".join(map(str,case['best']))))
                f.write("{},{}\n".format(rowName + ' worst', ",".join(map(str,case['worst']))))
                f.write("{},{}\n".format(rowName + ' average', ",".join(map(str,case['average']))))

