def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffmat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        votaIlabel = labels[sortedDistIndicies[i]]
        classCount[votaIlabel] = classCount.get(votaIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]